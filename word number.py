__author__ = 'JJW'

import re


def word_number(fname):
    with open(fname, 'r') as f:
        result = {}
        s = f.read()
        list_word = re.split(' |\n', s)
        for word in list_word:
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
        print(result)
word_number('aa.txt')