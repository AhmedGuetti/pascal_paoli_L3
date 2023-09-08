'''
Author: Ahmed Guetti
Atelir: 2
date: 08/09/2023

exercice 1
'''

# Question 1

'''


solution 2:
    def somme(L: list, test_type: float)->float:
        lenght = len(L)
        somme = 0
        if test_type == 1:
            for i in range(lenght):
                somme += L[i]
        elif test_type == 2:
            for element in L:
                somme+=element
        elif test_type == 3:
            i=0
            while i < len(L):
                somme += L[i]
                i += 1
        else:
            return "[Test Type Error]"
        return somme

    def test_exercice1 ():
        print("TEST SOMME")
            #test liste vide
        print("[Type 1] Test liste vide : ", somme([], 1))
        print("[Type 2] Test liste vide : ", somme([], 2))
        print("[Type 3] Test liste vide : ", somme([], 3))
            #test somme 11111
        lst2test1=[1,10,100, 1000,10000]
        print("[Type 1]Test somme 1111 : ", somme(lst2test1, 1))
        print("[Type 2]Test somme 1111 : ", somme(lst2test1, 2))
        print("[Type 3]Test somme 1111 : ", somme(lst2test1, 3))
'''



def somme_1(L: list):
    somme = 0
    for i in range(len(L)):
        somme += L[i]
    return somme

def somme_2(L:list):
    somme = 0
    for element in L:
        somme+=element
    return somme

def somme_3(L:list):
    somme = indice = 0
    while indice < len(L):
        somme += L[indice]
        indice += 1
    return somme



#Question 2
def test_exercice1 ():
    print("TEST SOMME")
    #test liste vide
    print("[Type 1] Test liste vide : ", somme_1([]))
    print("[Type 2] Test liste vide : ", somme_2([]))
    print("[Type 3] Test liste vide : ", somme_3([]))
    #test somme 11111
    lst2test1=[1,10,100, 1000,10000]
    print("[Type 1]Test somme 1111 : ", somme_1(lst2test1))
    print("[Type 2]Test somme 1111 : ", somme_2(lst2test1))
    print("[Type 3]Test somme 1111 : ", somme_3(lst2test1))

test_exercice1()

# Question3
def moyenne (L:list)->float:
    lenght = len(L)
    moy = 0 
    if lenght != 0:
        somme = somme_2()
        moy = somme / lenght
        return moy        
    return 0

# Question 4
def nb_sup_1(L:list,e:int):
    count = 0
    for i in range(len(L)):
       if L[i] > e:
           count += 1
    return count

def nb_sup_2(L:list,e:int):
    count = 0
    for element in L:
       if element > e:
           count += 1
    return count


#Question 5

def moy_sub(L:list,e:int):
    new_list = []
    for element in range(len(L)):
        if element > e:
            new_list.append(element)
    return moyenne(new_list)

# Question 6
''' 
    Fonction pour trouver la valeur maximal d'un List
'''
def val_max(L:list)->int:
    if len(L) != 0:
        max = L[0]
        for e in L:
            if e > max:
                max = e
        return max
    return None


#Question 7
''' 
    un Fonction qui return l'indice maximal d'un element dans un List 
    On itilisant La Fonction <<List.index>>

    solution 2:
        def ind_max(L:list)->int:
        lenght = 0
        if lenght != 0:
            ind_max = 0
            for i in range(lenght):
                if L[ind_max] < L[i]:
                    ind_max = i
            return ind_max
        return None

'''
def ind_max(L:list)->int:
   max_val = val_max(L)
   return L.index(max_val)
