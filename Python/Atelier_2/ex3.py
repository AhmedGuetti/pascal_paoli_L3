'''
Author: Ahmed Guetti
Atelir: 2
date: 08/09/2023

exercice 3
'''
import random
def separer(L:list)->list:
    """
    une fontion qui vas separe une list en trois categorie [negatif, null, positif]
    exemple:
        input:  [32,43,0,2,0,-1,32,-43,-5,2,0]
        output: [-1,-43,-5,0,0,0,32,43,2,32,2]

    Args:
        L (list): une Liste pour le separe

    Returns:
        list: la list resultat 
    """
    LSEP = []
    negatif =[] 
    null = [] 
    positif = []
    for e  in L:
        if e < 0:
            negatif.append(e)
        elif e > 0:
            positif.append(e)
        else:
            null.append(e)
    LSEP.extend(negatif)
    LSEP.extend(null)
    LSEP.extend(positif)
    return LSEP    


def testing_unit (L:list):
    """
    une fontion de test tres simple 

    Args:
        L (list): une list pour le separe 
    """
    print(f"[Init List] separe({L}) =====> {separer(L)}")

def main():
    """
    la fonction main qui sera notre point d'enter pour tester tous les cas possible
    """
    list1 = [12,41,-43,0,-43,5,-6,0,12,55,-54,0]
    testing_unit(list1)
    randomlist = []
    for i in range(0,5):
        n = random.randint(1,30)
        randomlist.append(n)
        testing_unit(randomlist)

if __name__ == "__main__":
    main()