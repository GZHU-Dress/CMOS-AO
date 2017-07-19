"""https://github.com/CzRzChao/SimpleGA"""
# coding=utf-8
# !/usr/bin/env python


import matplotlib.pyplot as plt
import math
import random


def b2d(b, max_value, chrom_length):
    """计算二进制序列代表的数值"""
    t = 0
    for j in range(len(b)):
        t += b[j] * (math.pow(2, j))
    t = t * max_value / (math.pow(2, chrom_length) - 1)
    return t


def genEncoding(pop_size=50, chrom_length=10):
    """编码"""
    pop = [[]]
    for i in range(pop_size):
        temp = []
        for j in range(chrom_length):
            temp.append(random.randint(0, 1))
        pop.append(temp)
    return pop[1:]


def decodechrom(pop, chrom_length):
    """解码"""
    temp = []
    for i in range(len(pop)):
        t = 0
        for j in range(chrom_length):
            t += pop[i][j] * (math.pow(2, j))
        temp.append(t)
    return temp


def calobjValue(pop, chrom_length, max_value):
    """个体评价"""
    temp = []
    obj_value = []
    temp = decodechrom(pop, chrom_length)
    for i in range(len(temp)):
        x = temp[i] * max_value / (math.pow(2, chrom_length) - 1)
        obj_value.append(10 * math.sin(5 * x) + 7 * math.cos(4 * x))
    return obj_value


def calfitValue(obj_value):
    """淘汰(去除负值)"""
    fit_value = []
    c_min = 0
    for i in range(len(obj_value)):
        if (obj_value[i] + c_min > 0):
            temp = c_min + obj_value[i]
        else:
            temp = 0.0
        fit_value.append(temp)
    return fit_value


def best(pop, fit_value):
    """选优"""
    px = len(pop)
    best_individual = []
    best_fit = fit_value[0]
    for i in range(1, px):
        if (fit_value[i] > best_fit):
            best_fit = fit_value[i]
            best_individual = pop[i]
    return [best_individual, best_fit]


def sum(fit_value):
    """求和"""
    total = 0
    for i in range(len(fit_value)):
        total += fit_value[i]
    return total


def cumsum(fit_value):
    """计算累计概率"""
    for i in range(len(fit_value) - 2, -1, -1):  # 以-1为步长
        t = 0
        j = 0
        while(j <= i):
            t += fit_value[j]
            j += 1
        fit_value[i] = t
        fit_value[len(fit_value) - 1] = 1


def selection(pop, fit_value):
    """新的种群"""
    newfit_value = []
    total_fit = sum(fit_value)  # 适应度总和
    for i in range(len(fit_value)):
        newfit_value.append(fit_value[i] / total_fit)
    # 计算累计概率
    cumsum(newfit_value)
    ms = []
    pop_len = len(pop)
    for i in range(pop_len):
        ms.append(random.random())
    ms.sort()  # 排序
    fitin = 0
    newin = 0
    newpop = pop
    # 轮盘选择法
    while newin < pop_len:
        if (ms[newin] < newfit_value[fitin]):
            newpop[newin] = pop[fitin]
            newin += 1
        else:
            fitin += 1
    pop = newpop


def crossover(pop, pc):
    """交配"""
    pop_len = len(pop)
    for i in range(pop_len - 1):
        if(random.random() < pc):
            cpoint = random.randint(0, len(pop[0]))
            temp1 = []
            temp2 = []
            temp1.extend(pop[i][0:cpoint])
            temp1.extend(pop[i + 1][cpoint:len(pop[i])])
            temp2.extend(pop[i + 1][0:cpoint])
            temp2.extend(pop[i][cpoint:len(pop[i])])
            pop[i] = temp1
            pop[i + 1] = temp2


def mutaion(pop, pm):
    """变异"""
    px = len(pop)
    py = len(pop[0])

    for i in range(px):
        if(random.random() < pm):
            mpoint = random.randint(0, py - 1)
            if(pop[i][mpoint] == 1):
                pop[i][mpoint] = 0
            else:
                pop[i][mpoint] = 1


pop_size = 500  # 种群数量
max_value = 15  # 基因种允许出现的最大值
chrom_length = 15  # 染色体长度
pc = 0.8  # 交配概率
pm = 0.01  # 变异概率
results = [[]]  # 存储每一代的最优解，N个二元组
fit_value = []  # 个体适应度
fit_mean = []  # 平均适应度

pop = genEncoding(pop_size, chrom_length)
for i in range(pop_size):
    obj_value = calobjValue(pop, chrom_length, max_value)  # 个体评价
    fit_value = calfitValue(obj_value)  # 淘汰
    best_individual, best_fit = best(pop, fit_value)  # 选优，储存最优解和最优基因
    results.append([best_fit, b2d(best_individual, max_value, chrom_length)])
    selection(pop, fit_value)  # 新种群复制
    crossover(pop, pc)  # 交配
    mutaion(pop, pm)  # 变异
results = results[1:]
results.sort()
print('results[-1]', results[-1], '|', 'best_individual',
      best_individual, '|', 'best_fit',
      best_fit, '|', 'obj_value[1]', obj_value[1])
print('results', results)
print("y = %f, x = %f" % (results[-1][0], results[-1][1]))

X = []
Y = []
for i in range(500):
    X.append(i)
    t = results[i][0]
    Y.append(t)

plt.plot(X, Y)

plt.show()
