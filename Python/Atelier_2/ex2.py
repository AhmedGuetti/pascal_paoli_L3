'''
Author: Ahmed Guetti
Atelir: 2
date: 08/09/2023

exercice 2
'''
import math

def position_1(lst: list, elt: int) -> int:
    """
    Trouve la première position d'un élément dans une liste.

    Args:
        lst (list): La liste d'entiers.
        elt (int): L'élément à rechercher dans la liste.

    Returns:
        int: La première position de l'élément dans la liste, ou -1 si l'élément n'est pas trouvé.
    """
    ans = -1
    for i, e in enumerate(lst):
        if e == elt:
            ans = i
            break
    return ans

def position_2(lst: list, elt: int) -> int:
    """
    Trouve la première position d'un élément dans une liste.

    Args:
        lst (list): La liste d'entiers.
        elt (int): L'élément à rechercher dans la liste.

    Returns:
        int: La première position de l'élément dans la liste, ou -1 si l'élément n'est pas trouvé.
    """
    exist = False
    ans = -1
    while not exist:
        ans += 1
        if lst[ans] == elt:
            exist = True
    return ans

def nb_occurrences(lst: list, e: int) -> int:
    """
    Compte le nombre d'occurrences d'un élément dans une liste.

    Args:
        lst (list): La liste d'entiers.
        e (int): L'élément à compter dans la liste.

    Returns:
        int: Le nombre d'occurrences de l'élément dans la liste.
    """
    ans = 0
    for element in lst:
        if e == element:
            ans += 1
    return ans


def est_triee_1(lst:list)->bool:
    """
     une fonction pour tester si une list est triee

    Args:
        lst (list): une list pour le tester la fonction sure

    Returns:
        bool: le resultat de la list
    """
    lenght = len(lst)
    ans = True
    if lenght != 0 and lenght != 1:
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                ans = False
                break
    return ans


def est_triee_2(lst:list)->bool:
    """
     une fonction pour tester si une list est triee
     V2

    Args:
        lst (list): une list pour le tester la fonction sure

    Returns:
        bool: le resultat de la list
    """
    i = 0
    lenght = len(lst)
    ans = True
    while i < lenght - 1 or not ans:
        if lst[i] > lst[i+1]:
            ans = False
            break
        i+=1
    return ans



import math

def position_tri(lst: list, e: int) -> int:
    """
    Trouve la position d'un élément dans une liste triée par recherche binaire.

    Args:
        lst (list): La liste triée d'entiers.
        e (int): L'élément à rechercher dans la liste.

    Returns:
        int: La position de l'élément dans la liste, ou -1 si l'élément n'est pas trouvé.
    """
    left = 0
    right = len(lst) - 1
    while left <= right:
        m = math.floor((left + right) / 2)
        if lst[m] < e:
            left = m + 1
        elif lst[m] > e:
            right = m - 1
        else:
            return m
    return -1

def a_repetitions(lst: list) -> bool:
    """
    Vérifie si une liste contient des éléments en répétition.

    Args:
        lst (list): La liste d'entiers.

    Returns:
        bool: True si des éléments sont en répétition dans la liste, False sinon.
    """
    new_list = []
    i = 0
    length = len(lst)
    ans = False
    while i < length:
        if lst[i] not in new_list:
            new_list.append(lst[i])
        else:
            ans = True
            break
        i += 1
    return ans






