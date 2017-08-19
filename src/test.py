# -*- coding: utf-8 -*-
# !/usr/bin/env python

import re


class GA(object):

    def __init__(self, path, gene_w, gene_l):
        self.path = path
        self.gene_w = gene_w
        self.gene_l = gene_l


class IOFILE(GA):
    def read(self):
        num = 0
        name = []
        with open(self.path, 'r') as f:
            while True:
                line = f.readline()
                if line == '':
                    break
                tmp = line.split()
                if tmp != []:
                    if re.match('M', tmp[0].upper()):
                        num += 1
        return num


path = 'data/netlist'
gene_w = 19
gene_l = 13
NUM = GA(path, gene_w, gene_l)
print(IOFILE.read(NUM))
