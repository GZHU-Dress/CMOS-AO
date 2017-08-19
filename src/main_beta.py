#!/usr/bin/python3
# -*- coding: utf-8 -*-

import ga_beta
from ga_beta import GA

path = 'data/netlist'
gene_w = 19
gene_l = 13
pop_size = 500
max_value = 15
pc = 0.8
pm = 0.01
INFO = GA(path, gene_w, gene_l, pop_size, pc, pm, max_value)
tmp = GA.calobjvalue(INFO)
