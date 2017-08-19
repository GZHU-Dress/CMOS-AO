# coding=utf-8

from read_data import read
from ga import *
import matplotlib.pyplot as plt
import os

gene_w = 19  # MOS 管寬度 范围为 0um 至 9999.99um 精度 0.1um
gene_l = 13  # MOS 管長度 范围为 0um 至 99.99um 精度 0.1um
num = read('data/xidiancmos.sp')  # num MOS管数量
pop_size = 500
pc = 0.8
pm = 0.01
fit_value = []
fit_mean = []
results = [[]]
max_value = 15

chrom_length = (gene_w + gene_l) * num  # 染色体长度
pop.encoding(pop_size, chrom_length)
print(pop)

# for i in range(pop_size):
#     obj_value = calobjvalue(pop_size, pop, chrom_length, max_value,
#                             gene_w, gene_l, num)  # 个体评价
    # fit_value = calfitvalue(obj_value)  # 淘汰
    # best_individual, best_fit = best(pop, fit_value)  # 选优，储存最优解和最优基因
    # results.append([best_fit, b2d(best_individual, max_value, chrom_length)])
    # selection(pop, fit_value)  # 新种群复制
    # crossover(pop, pc)  # 交配
    # mutaion(pop, pm)  # 变异
# results = results[1:]
# results.sort()
# print(results)
# print('results[-1]', results[-1], '\n', 'best_individual',
#       best_individual, '\n', 'best_fit',
#       best_fit, '\n', 'obj_value[1]', obj_value[1])
# print('results', results)
# print("y = %f, x = %f" % (r`esults[-1][0], results[-1][1]))

# X = []
# Y = []
# for i in range(pop_size):
#     X.append(i)
#     t = results[i][0]
#     Y.append(t)
#
# plt.plot(X, Y)
#
# plt.show()
