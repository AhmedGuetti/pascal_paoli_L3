import time
import random
import math as m
import matplotlib.pyplot as plt
import numpy as np

import partie1


def perf_mix(mix_me: callable, mix_py: callable, lists_size: list, nb: int) -> tuple:
    """
    Mesure les performances de deux fonctions de mélange pour différentes tailles de listes.

    Args:
        mix_me (callable): La fonction de mélange à tester (implémentation personnalisée).
        mix_py (callable): La fonction de mélange à tester (implémentation Python standard).
        lists_size (list): Liste des tailles de listes à tester.
        nb (int): Le nombre de fois que chaque mélange est exécuté pour calculer la moyenne.

    Returns:
        tuple: Un tuple contenant deux listes, l'une pour les temps d'exécution de mix_me et l'autre pour mix_py.
    """
    ans = ([], [])
    for size in lists_size:
        moy_me = 0
        moy_py = 0
        for j in range(nb):
            L = partie1.gen_list_random_int(size, 0, size * 2)
            start_pc = time.perf_counter()
            mix_me(L)
            end_pc = time.perf_counter()

            start_pc_py = time.perf_counter()
            mix_py(L)
            end_pc_py = time.perf_counter()

            moy_me += end_pc - start_pc
            moy_py += end_pc_py - start_pc_py
        moy_me = moy_me / nb
        moy_py = moy_py / nb
        ans[0].append(moy_me)
        ans[1].append(moy_py)
    return ans


def perf_extract(extract_elements_list: callable, sample: callable, lists_size: list, nb: int) -> tuple:
    """
    Mesure les performances de deux fonctions d'extraction d'éléments pour différentes tailles de listes.

    Args:
        extract_elements_list (callable): La fonction d'extraction à tester (implémentation personnalisée).
        sample (callable): La fonction d'extraction à tester (implémentation Python standard).
        lists_size (list): Liste des tailles de listes à tester.
        nb (int): Le nombre de fois que chaque extraction est exécutée pour calculer la moyenne.

    Returns:
        tuple: Un tuple contenant deux listes, l'une pour les temps d'exécution de extract_elements_list et l'autre pour sample.
    """
    ans = ([], [])
    for size in lists_size:
        moy_me = 0
        moy_py = 0
        for j in range(nb):
            L = partie1.gen_list_random_int(size, 0, size * 2)
            start_pc = time.perf_counter()
            extract_elements_list(L, m.floor(random.random() * size))
            end_pc = time.perf_counter()

            start_pc_py = time.perf_counter()
            sample(L, m.floor(random.random() * size))
            end_pc_py = time.perf_counter()

            moy_me += end_pc - start_pc
            moy_py += end_pc_py - start_pc_py
        moy_me = moy_me / nb
        moy_py = moy_py / nb
        ans[0].append(moy_me)
        ans[1].append(moy_py)
    return ans


def testing_unit_mix():
    """
    Effectue des tests de performance pour les fonctions de mélange.

    Returns:
        None
    """
    lists_size = [10, 500, 5000, 50000, 100000]
    timeming = perf_mix(partie1.mix_list, random.shuffle, lists_size, 10)
    print(timeming[0])
    print(timeming[1])

    fig, ax = plt.subplots()

    ax.plot(lists_size, timeming[0], 'bo-', label='partie1.mix_list')
    ax.plot(lists_size, timeming[1], 'r*-', label='random.shuffle')
    ax.set(xlabel='nombre de test', ylabel="temps d'exécution",
           title='le temps d\'exécution pour différentes fonctions')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()


def testing_unit_extract():
    """
    Effectue des tests de performance pour les fonctions d'extraction d'éléments.

    Returns:
        None
    """
    lists_size = [10, 500, 5000, 50000, 100000]
    timeming = perf_extract(partie1.extract_elements_list_v3, random.sample, lists_size, 50)
    timeming1 = perf_extract(partie1.extract_elements_list_v2, partie1.extract_elements_list_v1, lists_size, 50)
    timeming2 = perf_extract(partie1.extract_elements_list, random.sample, lists_size, 50)

    print(f"extract v3 {timeming[0]}")
    print(f"extract v2 {timeming1[0]}")
    print(f"extract v1 {timeming1[1]}")
    print(f"extract v0 {timeming2[0]}")
    print(f"sample {timeming[1]}")

    fig, ax = plt.subplots()

    ax.plot(lists_size, timeming[0], 'bo-', label='partie1.extract_elements_list')
    ax.plot(lists_size, timeming[1], 'r*-', label='random.sample')
    ax.set(xlabel='nombre de test', ylabel="temps d'exécution",
           title='le temps d\'exécution pour différentes fonctions')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()


def main():
    testing_unit_extract()


if __name__ == "__main__":
    main()
