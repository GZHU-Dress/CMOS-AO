# -*- coding: utf-8 -*-
# !/usr/bin/env python

import re
import random
import math
import os
import time


class GA(object):
    def __init__(self, path, gene_w, gene_l, pop_size, pc, pm, max_value):
        self.path = path
        self.gene_w = gene_w
        self.gene_l = gene_l
        self.pop_size = pop_size
        self.pc = pc
        self.pm = pm
        self.max_value = max_value
        self.num = FILEIO.read(self)
        self.chrom_length = (self.gene_w + self.gene_l) * self.num

    def encoding(self):
        pop = [[]]
        for i in range(self.pop_size):
            tmp = []
            for j in range(self.chrom_length):
                tmp.append(random.randint(0, 1))
            pop.append(tmp)
        return pop[1:]

    def decoding(self, single):
        gene_sum = self.gene_w + self.gene_l
        tmp = []
        for i in range(self.num):
            mos = single[gene_sum * i:gene_sum * (i + 1)]
            W = L = 0
            for j in range(self.gene_l):
                L += mos[- j - 1] * (math.pow(2, j))
            for q in range(self.gene_l, gene_sum):
                W += mos[- q - 1] * (math.pow(2, q - self.gene_l))
            tmp.append([W, L])
        return tmp

    def calobjvalue(self):
        tmp = []
        obj_value = []
        pop = GA.encoding(self)
        print(pop)
        for i in range(self.pop_size):
            tmp = GA.decoding(self, pop[i])
            print('\n %s' % tmp)
            FILEIO.write(self, tmp)
            # time.sleep(1)
            # try:
            #     # call your program here.
            #     os.popen("ngspice -ars -c data/opamp2_ldo_cq_mf.sp")
            #     results = analysing(self, self.path)
            # except OSError:
            #     pass
        # return results

    def training(self):
        """Analyzing the command output and calculating the score."""
        for i in range(self.pop_size):
            obj_value = calobjvalue(self)


class FILEIO(GA):
    def read(self):
        """Read the number of MOS."""
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

    def change(value):
        def replace(x):
            return '{}{}{}{}'.format(
                x.group(1), value[0] / 100, x.group(3), value[1] / 100)  # 恢復精度
        return replace

    def write(self, data):
        """Write data to netlist"""
        pattern = r'(W=)(\d*\.?\d+)(.*L=)(\d*\.?\d+)'
        with open(self.path, 'r') as f:
            count = 0
            lines = f.readlines()
            for i in range(len(lines)):
                tmp = lines[i].split()
                if tmp != []:
                    if re.match('M', tmp[0].upper()):
                        lines[i] = re.sub(
                            pattern, FILEIO.change(data[count]), lines[i])
                        count += 1

        with open(self.path, 'w') as f:
            try:
                f.writelines(lines)
                print('New netlist file has been generated！')
            except IOError:
                print('Failed to generate the newlist.')

    def analysing(self):
        path = 'data/score'
        with open(path, 'r') as f:
            lines = f.readlines
            for i in range(len(lines)):
                tmp = lines[i].split()
                if tmp != []:
                    print(tmp)
