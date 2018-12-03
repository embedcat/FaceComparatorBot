import time


class BotLogger:
    silent, nosavelog, file = False, False, "log.txt"

    def __init__(self, silent=False, nosavelog=False, file="log.txt", startparams=""):
        self.silent = silent
        self.nosavelog = nosavelog
        self.file = file
        self.log("Bot has been start")
        if startparams:
            self.log("Started with arguments: " + str(startparams))

    def log(self, msg, user=None, reply=""):
        if user:
            text = "<" + str(user) + ">: " + str(msg) + "\n<Bot reply>: " + str(reply) + "\n"
        else:
            text = msg
        self._save(text=text)

    def _save(self, text):
        pref = self._makeLogPrefix()
        if not self.silent:
            print(pref, text)
        if not self.nosavelog:
            with open(self.file, 'a') as f:
                f.write(pref + text + "\n")

    def _makeLogPrefix(self):
        cur_date = time.strftime("%D")
        cur_time = time.strftime("%H:%M:%S")
        return "----------\n" + str(cur_date) + " " + str(cur_time) + "\n"
