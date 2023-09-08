'''
Author: Ahmed Guetti
Atelir: 2
date: 08/09/2023

exercice 2
'''

'''
fonction qui retourn l'indice du element elt.
Condition:
    --> si elt n'exist pas dans lst on retourn -1
    --> les valeur du list sont unique
    --> la list n'est pas triée
'''


def position_1(lst:list,elt:int)->int:
    ans = -1
    for e, i in enumerate(lst):
        if e == elt:
            ans = i
    return ans

def position_2(lst:list,elt:int)->int:
    exist = False
    ans = -1
    while not exist:
        ans += 1
        if lst[ans] == elt:
            exist = True
            return ans
    return ans


'''
    une fonction qui retourn le nombre d'occurence d'un valeur dans un List
    Condition:
        --> la list peut avoir des répétitions
        --> la list n'est pas triee

'''

def nb_occurrences(lst:list,e:int)->int:
    ans = 0
    for element in lst:
        if e == element:
            ans += 1
    return ans




