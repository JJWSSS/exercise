__author__ = 'JJW'
# -*- coding: utf-8 -*-

import os


def list_all(keyword):
    current_dir = os.listdir('.')
    history_list = []
    all_dir = []
    for dirl in current_dir:
        history_list.append('.')
        all_dir.append(dirl)
    history_list1 = []
    all_dir1 = []
    while not all_dir:
        for i in range(0, len(all_dir)):
            now = os.path.join(history_list[i], all_dir[i])
            if os.path.isdir(now):
                for dirl in os.listdir(now):
                    history_list1.append(now)
                    all_dir1.append(dirl)
            else:
                


