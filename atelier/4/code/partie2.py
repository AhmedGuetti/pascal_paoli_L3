import time
import random
import math as m
import matplotlib.pyplot as plt
import numpy as np


import partie1


def perf_mix(mix_me:callable, mix_py:callable, lists_size:list, nb:int)->tuple:
    ans = ([],[])
    for size in  lists_size:
        moy_me = 0
        moy_py = 0
        for j in range(nb):
            L = partie1.gen_list_random_int(size,0,size*2)
            start_pc = time.perf_counter()
            mix_me(L)
            end_pc = time.perf_counter()

            start_pc_py = time.perf_counter()
            mix_py(L)
            end_pc_py = time.perf_counter()


            moy_me += end_pc-start_pc
            moy_py += end_pc_py-start_pc_py
        moy_me = moy_me / nb
        moy_py = moy_py / nb
        ans[0].append(moy_me)
        ans[1].append(moy_py)
    return ans

def perf_extract(extract_elements_list:callable, sample:callable, lists_size:list, nb:int)->tuple:
    ans = ([],[])
    for size in  lists_size:
        moy_me = 0
        moy_py = 0
        for j in range(nb):
            L = partie1.gen_list_random_int(size,0,size*2)
            start_pc = time.perf_counter()
            extract_elements_list(L, m.floor(random.random()*size))
            end_pc = time.perf_counter()

            start_pc_py = time.perf_counter()
            sample(L, m.floor(random.random()*size))
            end_pc_py = time.perf_counter()


            moy_me += end_pc-start_pc
            moy_py += end_pc_py-start_pc_py
        moy_me = moy_me / nb
        moy_py = moy_py / nb
        ans[0].append(moy_me)
        ans[1].append(moy_py)
    return ans











def testing_unit_mix():
    lists_size =  [10, 500, 5000, 50000, 100000]
    timeming = perf_mix(partie1.mix_list, random.shuffle, lists_size, 10)
    print(timeming[0])
    print(timeming[1])

    fig,ax = plt.subplots()

    ax.plot(lists_size,timeming[0],'bo-',label='partie1.mix_list')
    ax.plot(lists_size,timeming[1], 'r*-', label='random.shuffle')
    ax.set(xlabel='nombre de test', ylabel='temps d\'execution',
    title='le temps d\'execution pour different fonction')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    #fig.savefig("test.png")
    plt.show()

def testing_unit_extract():
    lists_size =  [10, 500, 5000, 50000, 100000]
    timeming = perf_extract(partie1.extract_elements_list_v2, random.sample, lists_size, 10)
    print(timeming[0])
    print(timeming[1])

    fig,ax = plt.subplots()

    ax.plot(lists_size,timeming[0],'bo-',label='partie1.extract_elements_list')
    ax.plot(lists_size,timeming[1], 'r*-', label='random.sample')
    ax.set(xlabel='nombre de test', ylabel='temps d\'execution',
    title='le temps d\'execution pour different fonction')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    #fig.savefig("test.png")
    plt.show()


def main():
    testing_unit_extract()


if __name__ == "__main__":
    main()