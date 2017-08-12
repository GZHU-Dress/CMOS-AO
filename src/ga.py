# coding=utf-8
import random
import math


def b2d(b, max_value, chrom_length):
    """计算二进制序列代表的数值"""
    t = 0
    for j in range(len(b)):
        t += b[j] * (math.pow(2, j))
    t = t * max_value / (math.pow(2, chrom_length) - 1)
    return t


def encoding(pop_size=50, chrom_length=10):
    """编码"""
    pop = [[]]
    for i in range(pop_size):
        tmp = []
        for j in range(chrom_length):
            tmp.append(random.randint(0, 1))
        pop.append(tmp)
    return pop[1:]


def decoding(pop_size,  pop, gene_w, gene_l, num):
    """解码"""
    gene_sum = gene_w + gene_l
    for i in range(pop_size):
        single = pop[i]
        tmp = []
        for j in range(num):
            mos = single[gene_sum * j:gene_sum * (j + 1)]
            W = L = 0
            for q in range(gene_l):
                L += mos[- q - 1] * (math.pow(2, q))
            for q in range(gene_l, gene_sum):
                W += mos[- q - 1] * (math.pow(2, q - gene_l))
            tmp.append([W, L])
            # todo: write tmp to file.
    print(tmp)


def calobjvalue(pop_size, pop, chrom_length, max_value, gene_w, gene_l, num):
    """个体评价"""
    tmp = []
    obj_value = []
    tmp = decoding(pop_size, pop, gene_w, gene_l, num)
    # print(tmp)
    # for i in range(len(tmp)):
    #     x = tmp[i] * max_value / (math.pow(2, chrom_length) - 1)
    #     obj_value.append(10 * math.sin(5 * x) + 7 * math.cos(4 * x))
    return obj_value


def calfitvalue(obj_value):
    """淘汰(去除负值)"""
    fit_value = []
    c_min = 0
    for i in range(len(obj_value)):
        if (obj_value[i] + c_min > 0):
            tmp = c_min + obj_value[i]
        else:
            tmp = 0.0
        fit_value.append(tmp)
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
            tmp1 = []
            tmp2 = []
            tmp1.extend(pop[i][0:cpoint])
            tmp1.extend(pop[i + 1][cpoint:len(pop[i])])
            tmp2.extend(pop[i + 1][0:cpoint])
            tmp2.extend(pop[i][cpoint:len(pop[i])])
            pop[i] = tmp1
            pop[i + 1] = tmp2


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
