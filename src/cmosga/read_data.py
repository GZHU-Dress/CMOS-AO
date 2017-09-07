# coding=utf-8
# !/usr/bin/env python


import os
import re


def read(path):
    data = []
    gene_w = 19  # 范围为 0um 至 9999.99um 精度 0.1um
    gene_l = 13  # 范围为 0um 至 99.99um 精度 0.1um
    with open(path, 'r') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            tmp = line.split()
            if tmp != []:
                if re.match('M', tmp[0]) or re.match('\*M', tmp[0]):
                    newtmp = [tmp[0]]
                    W = int(float(re.search('\d*\.?\d+',
                                            tmp[6:8][0]).group()) * 100)
                    W = '{0:0{gene}b}'.format(W, gene=gene_w)
                    L = int(float(re.search('\d*\.?\d+',
                                            tmp[6:8][1]).group()) * 100)
                    L = '{0:0{gene}b}'.format(L, gene=gene_l)
                    newtmp[len(newtmp):len(newtmp)] = [W, L]
                    data.append(newtmp)
    return data, gene_w, gene_l


if __name__ == '__main__':
    data = read('netlist')
    print(data)
    # for i in range(len(data[0])):
    #     print(data[0][i])
