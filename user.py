import os
import string
import random


class User:
    path = "./users/"
    cnt = 0
    file_name_template = "{path}{mark}_{n}.jpg"
    cur_mark = 0
    fc = None
    save_all_files = False

    def __init__(self, id, fc, save_all_files=True, user_name=None):
        self.path += str(id) + ("" if user_name is None else "_" + user_name) + "/"
        self.fc = fc
        self.save_all_files = save_all_files
        create_folder(self.path)

    def save_photo(self, downloaded_file, no):
        mark = id_generator(6) if self.save_all_files else "img"
        if no == 0:
            self.cur_mark = mark
        file_name = self.file_name_template.format(path=self.path, mark=self.cur_mark, n=no+1)
#        print(" >In save_photo(). Save photo to", self.path + file_name)
        with open(file_name, 'wb') as new_file:
            new_file.write(downloaded_file)

    def photo_process(self, downloaded_file):
        self.save_photo(downloaded_file, self.cnt)
        self.cnt += 1
        return self.cnt

    def compare(self):
        self.cnt = 0
        return self.fc.compare(self.file_name_template.format(path=self.path, mark=self.cur_mark, n=1),
                               self.file_name_template.format(path=self.path, mark=self.cur_mark, n=2))

    def get_cnt(self):
        return self.cnt

    def reset_cnt(self):
        self.cnt = 0


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' +  directory)


def id_generator(size, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == "__main__":
    print(os.listdir("./users/"))
    u = User("1234")
    print(os.listdir("./users/"))
