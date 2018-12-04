import const
from const import Msg as msgid
import telebot
import bot_logger
import facecomparator
import threading
import queue
import user
import time
import argparse
import bot_token


bot = telebot.TeleBot(bot_token.bot_token)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--silent", action="store_true", default=False)
    parser.add_argument("-l", "--no-save-log", action="store_true", default=False)
    parser.add_argument("-p", "--use-proxy", action="store_true", default=False)
    return parser


def do_work_thread():
    users = {}
    while True:
        item = q.get()
        if item is None:
            break
        file_id, chat_id = item[0], item[-1].chat.id
        user_name, user_id = item[-1].from_user.first_name, item[-1].from_user.id

        cur_user = users.setdefault(user_id, user.User(user_id, fc, user_name=user_name))
        downloaded_file = bot.download_file(bot.get_file(file_id).file_path)
        result = cur_user.photo_process(downloaded_file)

        bot.send_message(chat_id, msg_dict[msgid.msg_photo_received.value].format(cur_user.get_cnt()))
        log.log("<{}> File has been received.".format(user_name))

        if result > 1:
            bot.send_message(chat_id, msg_dict[msgid.msg_both_photos_received.value])
            log.log("<{}> Both file received. Start to proceed.".format(user_name))
            result = cur_user.compare()

            distance = result['distance']
            if distance:
                file1, file2 = result['file1'] + '.jpg', result['file2'] + '.jpg'
                photo1 = open(file1, 'rb')
                photo2 = open(file2, 'rb')
                bot.send_photo(chat_id, photo1, caption=msg_dict[msgid.msg_photo_detected_face.value] + str(1))
                bot.send_photo(chat_id, photo2, caption=msg_dict[msgid.msg_photo_detected_face.value] + str(2))
                decision = make_decision(distance)
                bot.send_message(chat_id, msg_dict[msgid.msg_euclidean_distance.value] + str(distance))
                bot.send_message(chat_id, decision)
                log.log("<{}> Distance: {}.".format(user_name, distance))
                log.log("<{}> Decision: {}.".format(user_name, decision))
                photo1.close()
                photo2.close()
            else:
                bot.send_message(chat_id, msg_dict[msgid.msg_face_detection_error.value].format(result['error']))
                log.log("<{}>".format(user_name) + msg_dict[msgid.msg_face_detection_error.value].format(result['error']))
        q.task_done()


def make_decision(dist):
    if dist == 0.0:
        return msg_dict[msgid.msg_decision_same_photos.value]
    if dist <= 0.55:
        return msg_dict[msgid.msg_decision_yes.value]
    if dist <= 0.6:
        return msg_dict[msgid.msg_decision_maybe.value]
    return msg_dict[msgid.msg_decision_no.value]


@bot.message_handler(content_types=['photo'])
def photo_handler(message):
    photo_sizes_cnt = len(message.photo)
    # for reduce photo size
    file_id = message.photo[photo_sizes_cnt-2].file_id
    item = [file_id, message]
    q.put(item)
    log.log(message.text, message.from_user.first_name, file_id)


@bot.message_handler(commands=['start'])
def reply_start(message):
    reply = msg_dict[msgid.msg_start.value]
    log.log(message.text, message.from_user.first_name, reply)
    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['en', 'ru'])
def reply_change_language(message):
    global msg_dict
    if message.text == "/en":
        msg_dict = const.english
    else:
        msg_dict = const.russian
    reply = msg_dict[msgid.msg_language_change.value]
    log.log(message.text, message.from_user.first_name, reply)
    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['about'])
def reply_about(message):
    reply = msg_dict[msgid.msg_about.value]
    log.log(message.text, message.from_user.first_name, reply)
    bot.send_message(message.chat.id, reply)


@bot.message_handler(commands=['help'])
@bot.message_handler(func=lambda message: True)
def reply_help(message):
    reply = msg_dict[msgid.msg_help.value]
    log.log(message.text, message.from_user.first_name, reply)
    bot.send_message(message.chat.id, reply)


if __name__ == "__main__":
    args = create_parser().parse_args()
    log = bot_logger.BotLogger(silent=args.silent, nosavelog=args.no_save_log, startparams=vars(args))
    if args.use_proxy:
        telebot.apihelper.proxy = const.proxylist

    fc = facecomparator.FaceCompare()
    msg_dict = const.russian

    q = queue.Queue()
    t1 = threading.Thread(target=do_work_thread)
    t1.start()
    while True:
        try:
            bot.polling()
        except Exception as e:
            log.log("Error: " + str(e))
            time.sleep(10)
