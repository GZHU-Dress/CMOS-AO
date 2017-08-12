# coding=utf-8
# !/usr/bin/env python


import os
import re


def read(path):
    num = 0
    name = []
    with open(path, 'r') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            tmp = line.split()
            if tmp != []:
                if re.match('M', tmp[0].upper()):
                    num += 1
    return num


if __name__ == '__main__':
    num = read(
        '/home/axionl/Documents/CMOS-AO/src/cmosga/netlist')
    print(num)
