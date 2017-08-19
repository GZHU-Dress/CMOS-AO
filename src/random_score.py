#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import os
import sys
import string
import re
import sqlite3
import time  # show
import inspect  # get var name


"""
standard:
    description: Get the standard data.
    path = 'data/standard'
    file: target_name-proportion(relative)-trend
    def:
        get_standard: Read the standard file.
    variable：
        st_path: eg: 'data/standard'
        st_name(standard target name): eg: ['L', 'I', ...]
        st_proportion(standard target relative proportion): eg: ['0.86', ...]
        st_trend(standard target developing trend): eg: ['+', '-', ...]
        st_data(standard_data): eg: [['l', '0.23221147168523082', '+'], ...]
result:
    description: Get the result data from ngspice.
    path = 'data/result'
    file = target_name-result_of_the_analysis
    def:
        init_result: Initializing data.(only need it for random testing)
        gen_result: Generate random result.(only need it for random testing)
        get_result: Read the result file.
    variable:
        rt_path: eg : 'data/result'
        rt_num: eg : 15 (only need it for random testing)
        rt_name(result target name): eg: ['L', 'I', ...]
        rt_value(result target value): eg: ['0.86', ...]
        rt_data(result): eg: [['L', '0.86'], ['J', '0.76'], ...]
        times: generating result times, eg:
            gen_result(rt_path, rt_name, times=1)
analysing:
    description: Compare the historical value and current value,
                calculate the final score.
    path = 'data/history.db'
    def:
        compare: compare the historical value and current value
        sql_write: write rt_data to sql
        sql_read: read rt_history from sql
    variable:
        db_path: eg: data/history.db
        rt_history(result target historical value): eg:
            [(1, 'L', 3.12), (2, 'I', 17.5), ...]
check:
    description: Check duplicate targets for file and return all targets.
    def:
        check: Check duplicate targets for st_data or rt_data.
        echo: Verbatim output effect.
    variable:
        data: incloud st_data or rt_data
        target: incloud st_name or rt_name
        speed: printing speed, eg: echo('test', 0.03)
sql:
    path = 'data/history.db'
    file:
        rt_history(table1):
        # standard(table2):
"""


def get_standard(st_path):
    pattern = r'([^\s])(,)(\d*\.?\d+)(,.*)([+-])'
    st_data = []
    with open(st_path, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            st_data[len(st_data):] = [[x for x in re.search(
                pattern, lines[i]).group(1, 3, 5)]]
        st_name = check(standard=st_data)
    return st_data, st_name


def init_result(rt_path, rt_num):
    rt_data = []
    rt_name = random.sample(string.ascii_uppercase, rt_num)
    for i in range(rt_num):
        rt_data.append(rt_name[i] + ' ' + str(random.random()) + '\n')
    with open(rt_path, 'w') as f:
        f.writelines(rt_data)
    return rt_name


def gen_result(rt_path, rt_name):
    rt_data = []
    for i in range(len(rt_name)):
        rt_data.append(rt_name[i] + ' ' + str(random.random()) + '\n')
    with open(rt_path, 'w') as f:
        f.writelines(rt_data)
    # print('Generating result', end='')
    # echo(' ...... ', 0.01)
    # print('[OK!]', end='\n')


def get_result(rt_path):
    rt_data = []
    with open(rt_path, 'r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            tmp = [lines[i].split()[0]] + [float(lines[i].split()[1])]
            if tmp != []:
                rt_data[len(rt_data):] = [tuple(tmp)]
                rt_num = len(rt_data)
        check(result=rt_data)
    return rt_data, rt_num


def compare(rt_data, rt_history, st_name, st_trend):
    # TODO: read all data from sqlite
    pass


def sql_creat(db_path):
    if os.path.isfile(db_path):
        choose = input('The database already exists, Overwrite or not? [Y/n] ')
        if choose == 'n':
            sys.exit(1)
        else:
            os.remove(db_path)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''CREATE TABLE `rt_history`
        (`id` INTEGER PRIMARY KEY ,
        `rt_name` TEXT NOT NULL COLLATE NOCASE,
        `rt_data` REAL);''')
    conn.commit()
    conn.close()


def sql_read(db_path, rt_num, times):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    count = rt_num * (times - 2)
    for row in c.execute(
            'SELECT `rt_name`,group_concat(`rt_data`) \
            FROM `rt_history` WHERE `id` > ? AND `id` < ? \
            GROUP BY `rt_name` ORDER BY `rt_name`;', (count, count * 3)):
        print(row)
    # 'SELECT rt_name,group_concat(rt_data) FROM rt_history GROUP BY rt_name')
    conn.close()


def sql_write(db_path, rt_data):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.executemany(
        'INSERT INTO rt_history(id, rt_name, rt_data) \
        VALUES (NULL, ?, ?);', rt_data)
    conn.commit()
    conn.close()


def check(**kwargs):
    target = []
    data = [value for value in kwargs.values()][0]
    for i in data:
        target.append(i[0])
    if len(data) != len(list(set(target))):
        print('Checking %s file' % [key for key in kwargs.keys()][0], end='')
        echo(' ...... ')
        print('[ERROR!]', end='\n')
        sys.exit(1)
    else:
        print('Checking %s file' % [key for key in kwargs.keys()][0], end='')
        echo(' ...... ')
        print('[OK!]', end='\n')
        return target


def echo(string, speed=0.03):
    for i in string:
        print(i, sep=' ', end='', flush=True)
        time.sleep(speed)


if __name__ == '__main__':
    st_path = '../data/standard'
    rt_path = '../data/result'
    db_path = '../data/history.db'
    times = 5
    rt_num = 3
    [st_data, st_name] = get_standard(st_path)
    sql_creat(db_path)
    rt_name = init_result(rt_path, rt_num)
    for i in range(times):
        gen_result(rt_path, rt_name)
        [rt_data, rt_num] = get_result(rt_path)
        sql_write(db_path, rt_data)
    sql_read(db_path, rt_num, times)
    # data = analysing(standard, targets)
