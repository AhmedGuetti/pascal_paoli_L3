import math
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


'''
    une fonction qui retourn True si la llist est triee et False dans l'autre cas
    Condition:
        --> version 1: une parcours systématique (boucle for)
        --> version 2: boucle while 
        --> la list doit etre triee croissant
'''

def est_triee_1(lst:list)->int:
    lenght = len(lst)
    ans = True
    if lenght != 0 and lenght != 1:
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                ans = False
    return ans


def est_triee_2(lst:list)->int:
    i = 0
    lenght = len(lst)
    ans = True
    while i < lenght - 1 or not ans:
        if lst[i] > lst[i+1]:
            ans = False
        i+=1
    return ans



def position_tri(lst:list,e:int)->int:
    left = 0
    right = len(lst) - 1
    while left < right:
        m = math.floor((left+right)/2)
        if lst[m] < e:
            left += m +1
        elif lst[m] > e:
            right -= m - 1
        else:
            return m
    return -1

# LIST = [12, 13, 14,16, 34,56,70]
# ans = position_tri(LIST, 100)
# print(ans)  


#Question 5
def a_repetitions(lst:list)->bool:
    new_list = []
    i = 0
    lenght = len(lst)
    ans = False
    while i <  lenght:
        if not (lst[i] in new_list):
            new_list.append(lst[i])
        else:
            ans = True
            break
    return ans






