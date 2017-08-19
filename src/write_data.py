# -*- coding: utf-8 -*-
# !/usr/bin/env python

import os
import re
from read_data import read


def change(value):
    def replace(x):
        return '{}{}{}{}'.format(
            x.group(1), value[0] / 100, x.group(3), value[1] / 100)  # 恢復精度
    return replace


def write(data, path, gene_w, gene_l):
    """Write data to netlist"""
    pattern = r'(W=)(\d*\.?\d+)(.*L=)(\d*\.?\d+)'
    with open(path, 'r') as f:
        count = 0
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i] == '':
                break
            tmp = lines[i].split()
            if tmp != []:
                if re.match('M', tmp[0]):
                    lines[i] = re.sub(pattern, change(data[count]), lines[i])
                    count += 1

    with open(path, 'w') as f:
        try:
            f.writelines(lines)
            print('New netlist file has been generated！')
        except IOError:
            print('Failed to generate the newlist.')


if __name__ == '__main__':
    path = 'data/netlist'
    gene_w = 19
    gene_l = 13
    data = [
        [45558.0, 3994.0],
        [66429.0, 675.0],
        [450593.0, 482.0],
        [193265.0, 3892.0],
        [32920.0, 5294.0],
        [494512.0, 7848.0],
        [138403.0, 4831.0],
        [138523.0, 2742.0],
        [234497.0, 2387.0],
        [229007.0, 2011.0],
        [434727.0, 4227.0],
        [28657.0, 5854.0],
        [331631.0, 6953.0],
        [392096.0, 5295.0]]  # result from decoding
    write(data, path, gene_w, gene_l)
