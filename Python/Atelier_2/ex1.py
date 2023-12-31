'''
Author: Ahmed Guetti
Atelier: 2
Date: 08/09/2023

Exercice 1
'''

def somme_1(L: list):
    """
    Calcule la somme des éléments d'une liste.

    Args:
        L (list): La liste d'entiers.

    Returns:
        int: La somme des éléments de la liste.
    """
    somme = 0
    for i in range(len(L)):
        somme += L[i]
    return somme

def somme_2(L: list):
    """
    Calcule la somme des éléments d'une liste (version simplifiée).

    Args:
        L (list): La liste d'entiers.

    Returns:
        int: La somme des éléments de la liste.
    """
    somme = 0
    for element in L:
        somme += element
    return somme

def somme_3(L: list):
    """
    Calcule la somme des éléments d'une liste (version avec une boucle while).

    Args:
        L (list): La liste d'entiers.

    Returns:
        int: La somme des éléments de la liste.
    """
    somme = indice = 0
    while indice < len(L):
        somme += L[indice]
        indice += 1
    return somme

def test_exercice1():
    print("TEST SOMME")
    # Test liste vide
    print("[Type 1] Test liste vide : ", somme_1([]))
    print("[Type 2] Test liste vide : ", somme_2([]))
    print("[Type 3] Test liste vide : ", somme_3([]))
    # Test somme 11111
    lst2test1 = [1, 10, 100, 1000, 10000]
    print("[Type 1] Test somme 11111 : ", somme_1(lst2test1))
    print("[Type 2] Test somme 11111 : ", somme_2(lst2test1))
    print("[Type 3] Test somme 11111 : ", somme_3(lst2test1))

# Question 3
def moyenne(L: list) -> float:
    """
    Calcule la moyenne des éléments d'une liste.

    Args:
        L (list): La liste d'entiers.

    Returns:
        float: La moyenne des éléments de la liste.
    """
    lenght = len(L)
    moy = 0
    if lenght != 0:
        somme = somme_2(L)
        moy = somme / lenght
    return moy

def test_exercice3():
    print("TEST MOYENNE")
    # Test liste vide
    print("Test liste vide : ", moyenne([]))
    # Test moyenne 11111
    lst2test1 = [1, 10, 100, 1000, 10000]
    print("Test moyenne : ", moyenne(lst2test1))

# Question 4
def nb_sup_1(L: list, e: int):
    """
    Compte le nombre d'éléments supérieurs à 'e' dans une liste.

    Args:
        L (list): La liste d'entiers.
        e (int): La valeur de référence.

    Returns:
        int: Le nombre d'éléments supérieurs à 'e'.
    """
    count = 0
    for i in range(len(L)):
        if L[i] > e:
            count += 1
    return count

def nb_sup_2(L: list, e: int):
    """
    Compte le nombre d'éléments supérieurs à 'e' dans une liste (version simplifiée).

    Args:
        L (list): La liste d'entiers.
        e (int): La valeur de référence.

    Returns:
        int: Le nombre d'éléments supérieurs à 'e'.
    """
    count = 0
    for element in L:
        if element > e:
            count += 1
    return count

def test_exercice4():
    print("TEST NB_SUP")
    print("[Type 1] Test liste vide : ", nb_sup_1([], 3))
    print("[Type 2] Test liste vide : ", nb_sup_2([], 3))
    lst2test1 = [1, 10, 100, 12, 32, 4, 1000, 10000]
    print("[Type 1] Test nb_sup : ", nb_sup_1(lst2test1, 3))
    print("[Type 2] Test nb_sup : ", nb_sup_2(lst2test1, 3))

# Question 5
def moy_sub(L: list, e: int):
    """
    Calcule la moyenne des éléments supérieurs à 'e' dans une liste.

    Args:
        L (list): La liste d'entiers.
        e (int): La valeur de référence.

    Returns:
        float: La moyenne des éléments supérieurs à 'e'.
    """
    if len(L) != 0:
        el_sup = nb_sup_1(L, e)
        ans = 0
        for element in L:
            if element > e:
                ans += element
        return ans / el_sup if el_sup != 0 else 0
    return -1

def test_exercice5():
    print("TEST Moy_sub")
    print("Test liste vide : ", moy_sub([], 3))
    lst2test1 = [1, 10, 100, 12, 32, 4, 1000, 10000]
    print("Test Moyen_sub : ", moy_sub(lst2test1, 3))

# Question 6
def val_max(L: list) -> int:
    """
    Trouve la valeur maximale dans une liste.

    Args:
        L (list): La liste d'entiers.

    Returns:
        int: La valeur maximale dans la liste.
    """
    if len(L) != 0:
        max = L[0]
        for e in L:
            if e > max:
                max = e
        return max
    return None


def test_exercice6 ():
    print("TEST val_max")
    print("Test liste vide : ", val_max([]))
    lst2test1=[1,10,100,12,32, 4, 1000,10000]
    print("Test val_max : ", val_max(lst2test1))


#Question 7
#     un Fonction qui return l'indice maximal d'un element dans un List 
#     On itilisant La Fonction <<List.index>>

#     solution 2:
#         def ind_max(L:list)->int:
#         lenght = 0
#         if lenght != 0:
#             ind_max = 0
#             for i in range(lenght):
#                 if L[ind_max] < L[i]:
#                     ind_max = i
#             return ind_max
#         return None

# 


def ind_max(L: list) -> int:
    """
    Trouve l'indice du maximum dans une liste.

    Args:
        L (list): La liste d'entiers.

    Returns:
        int: L'indice de la valeur maximale dans la liste, ou None si la liste est vide.
    """
    max_val = val_max(L)
    if max_val is not None:
        return L.index(max_val)
    return None

def test_exercice7 ():
    print("TEST ind_max")
    print("Test liste vide : ", ind_max([]))
    lst2test1=[1,10,100,12,32, 4, 1000,10000]
    print("Test ind_max : ", ind_max(lst2test1))






def testing():
    test_exercice1()
    test_exercice3()
    test_exercice4()
    test_exercice5()
    test_exercice6()
    test_exercice7()

def main():
    """
    la fonction main qui sera notre point d'enter pour tester tous les cas possible
    """
    testing()



if __name__ == "__main__":
    main()