import time


def log(msg, file="log.txt"):
    pref = _makeLogPrefix()
    print(pref, msg)
    with open(file, 'a') as f:
        f.write(pref + msg + "\n")


def log_error(e):
    log("Error while execute: " + str(e))


def makeLog(user, msg, reply):
    return "<" + str(user) + ">: " + str(msg) + "\n<Bot reply>: " + str(reply) + "\n"


def _makeLogPrefix():
    cur_date = time.strftime("%D")
    cur_time = time.strftime("%H:%M:%S")
    return "----------\n" + str(cur_date) + " " + str(cur_time) + "\n"


