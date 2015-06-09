__author__ = 'JJW'

import hashlib


md51 = hashlib.md5()
md51.update('how to start hashlib_test?'.encode('utf-8'))
print(md51.hexdigest())


class LogTest():
    def __init__(self):
        self.db = {}

    def register(self, username, password):
        self.db[username] = get_md5(str(password) + str(username) + 'the-Salt')

    def login(self, username, password):
        if username in self.db.keys():
            if self.db[username] == get_md5(str(password) + str(username) + 'the-Salt'):
                print('login success!')
            else:
                print('login failed!')
        else:
            print('username error!')


def get_md5(s):
    md5 = hashlib.md5()
    if isinstance(s, str):
        md5.update(s.encode('utf-8'))
        return md5.hexdigest()

l = LogTest()
l.register('Bob', 123)
l.login('Bob', 234)
l.login('Bob', 123)
l.login('JJW', 123)
