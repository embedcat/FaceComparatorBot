from enum import Enum, unique

bot_token = '486426595:AAF8DvlyoDMiKOAvErFkrZGLjRZg3sC9o8w'
file_with_face_suffix = "_face.jpg"


@unique
class Msg(Enum):
    msg_start = 0
    msg_help = 1
    msg_about = 2
    msg_photo_received = 3
    msg_both_photos_received = 4
    msg_euclidean_distance = 5
    msg_photo_detected_face = 6
    msg_face_detection_error = 7
    msg_decision_same_photos = 8
    msg_decision_yes = 9
    msg_decision_no = 10
    msg_decision_maybe = 11
    msg_language_change = 12


keys = ["msg_start",
        "msg_help",
        "msg_about",
        "msg_photo_received",
        "msg_both_photos_received",
        "msg_euclidean_distance",
        "msg_photo_detected_face",
        "msg_face_detection_error",
        "msg_decision_same_photos",
        "msg_decision_yes",
        "msg_decision_no",
        "msg_decision_maybe",
        "msg_language_change"]

english = ["Hello!\n"
           "I can recognize faces on photos and compare it.\n"
           "I make prediction - is two people on different photos the same or not.\n"
           "----------\n"
           "/help - how to use\n"
           "/about - more info about technologies\n"
           "/en - english language\n"
           "/ru - русский язык",

           "Help!",

           "About!",

           "Photo #{} has been received",

           "Both photos has been received. Start to proceed...\n"
           "Please wait...",

           "Euclidean distance between your photos: ",

           "Face detected on photo #",

           "Can't recognize face in file #{}!\n"
           "Please try another photo!",

           "Hm.. Looks like photos absolutely the same!\n"
           "Try different photos!",

           "People on photos definitely the same!",

           "Sorry, people on photos are different!",

           "Don't sure... People on photos are very similar!..",

           "Language has been changed to English."]

russian = ["Привет!\n"
           "Я умею распозновать лица на фотографиях и сравнивать их.\n"
           "Я делаю вывод - одинаковые ли люди на двух фотографиях.\n"
           "Пришлите мне 2 фотографии с лицами людей, которых необходимо сравнить.\n"
           "----------\n"
           "/help - как пользоваться\n"
           "/about - больше информации о технологиях\n"
           "/en - english language\n"
           "/ru - русский язык",

           "Как пользоваться?\n"
           "Пришлите мне 2 фотографии с лицами людей, которых необходимо сравнить.\n"
           "Если на фото несколько людей, то лицо выбирается случайно, так что используйте фотографии с одним человекм "
           "или отредактируйте её.\n"
           "После обработки фотографий нейросетью, выдаются фото распознанных лиц, а также эвклидово расстояние между "
           "векторами моделей распознанных лиц. Считается, что если это число меньше 0.6, то на фотографиях один и тот "
           "же человек. Чем ближе это число к 0, тем меньше различий между моделями лиц.",

           "Алгоритм использует технологию глубоких нейронных сетей для распознования лиц и построения их моделей.\n"
           "В качестве библиотеки машинного обучения используется dlib (http://dlib.net/)\n",

           "Получено фото #{} ",

           "Обе фотографии получены. Начинаю вычисления...\n"
           "Секундочку...",

           "Эвклидово расстояние между моделями лиц: ",

           "Распознанное лицо на фото #",

           "Не могу определить лицо на фото #{}!\n"
           "Попробуйте другое фото!",

           "Хм... Кажется фотографии абсолютно одинаковые!\n"
           "Попробуйте разные фото!",

           "Определённо, на фотографиях один и тот же человек!",

           "Извините, на фотографиях разные люди!",

           "Не уверен... Люди на фотографиях очень похожи!..",

           "Поменял язык на русский."]
