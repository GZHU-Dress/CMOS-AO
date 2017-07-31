# coding=utf-8
# !/usr/bin/env python


import os
import re

root = os.getcwd()
path = root + '/src/simplega/'
data = []
with open(path + 'netlist', 'r') as f:
    while True:
        line = f.readline()
        if line == '':
            break
        tmp = line.split()
        if tmp != []:
            if re.match('M', tmp[0]) or re.match('\*M', tmp[0]):
                newtmp = [tmp[0]]
                W = float(re.search('\d+', tmp[6:8][0]).group())
                L = float(re.search('\d+', tmp[6:8][1]).group())
                newtmp[len(newtmp):len(newtmp)] = [W, L]
                data.append(newtmp)

for i in range(len(data)):
    print(data[i])
