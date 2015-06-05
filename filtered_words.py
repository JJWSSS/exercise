__author__ = 'JJW'
# -*- coding: utf-8 -*-
import re


def filtered_words(word):
    with open('filtered_words.txt', 'r', encoding='utf-8') as f:
        s = f.read()
        words = re.split(' |\n', s)
        print(words)
        for fword in words:
            print(fword)
            if word.__contains__(fword):
                # if word == fword:
                print('Freedom')
                replace_string = ''
                for i in range(0, len(fword)):
                    replace_string += '*'
                print(word.replace(fword, replace_string))
                return
    print('Human Rights')
    print(word)
    return


filtered_words('北京')
