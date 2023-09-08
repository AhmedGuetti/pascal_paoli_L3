import random
'''
Author: Ahmed Guetti
Atelir: 2
date: 08/09/2023

exercice 3
'''


def separer(L:list)->list:
    """
        __summary__
            __parameter__:
                . L (list) the unsorted intial list
            __return__:
                .LSEP (list) a sorted list based of the negatif->null->positif

            __funcionality__:
                this function use three list to keep track of all three 
                value categorie then concatenate all three list into LESP
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
    print(f"[Init List] separe({L}) =====> {separer(L)}")

def main():
    """
        __summary__
            the main function that have the testing unit and doesn't 
            work when importing the module

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