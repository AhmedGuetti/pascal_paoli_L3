'''
Author: Ahmed Guetti
Atelir: 2
date: 09/09/2023

exercice 5
'''

def estetic (obj:list, nbEmplacement:int)->tuple:
    """
    une fonction qui simule un exemple réel d'un algorithme
    exemple:
        input:  objs:=[1,2,2,3,4,5,5], nbEmplacement:=4
        output: ([1,2,3,5], [2,4,5])
    Args:
        obj (list): list des Oject, element quelconque pour le stocker dans les deux vitrines
        nbEmplacement (int): nombre des place disponible dans chaque vitrine

    Returns:
        tuple: un tuple de deux list qui represent les deux vitrines 
    """
    obj.sort()

    
    vitrine_1 = [
        [], 
        nbEmplacement
    ]
    vitrine_2 = [[], nbEmplacement]
    trash = []
    # check = False
    i=0
    while i < len(obj)-1 and (vitrine_1[1] > 0 and vitrine_2[1] > 0):
        if i>0:
            if obj[i-1] == obj[i+1] == obj[i]:
                trash.append(obj[i])
                i+=1
                continue
        if obj[i] == obj[i+1]:
                vitrine_1[0].append(obj[i])
                vitrine_2[0].append(obj[i])
                vitrine_1[1] -= 1
                vitrine_2[1] -= 1
                i+=2
        else:
            if vitrine_1[1]  >= vitrine_2[1] or (vitrine_1[1]>0 and vitrine_2[1]<=0):
                vitrine_1[0].append(obj[i])
                vitrine_1[1] -= 1
            # elif vitrine_2[1]  >= vitrine_1[1] or (vitrine_2[1]>0 and vitrine_1[1]<=0):
            else:
                vitrine_2[0].append(obj[i])
                vitrine_2[1] -= 1
            i+=1
    if trash:
         print(f"[IMPOSSIBLE] TRASH: {trash}", end=" ") 
    return(vitrine_1[0], vitrine_2[0])







def main():
    """
    la fonction main qui sera notre point d'enter pour tester tous les cas possible
    """
    test_list = [
        ([1,2,2,3,4,5,5],4),
        ([],5),
        ([2,2,2,2,2,2,2], 5),
        ([1,2,4,4,5,6,7], 3),
        ([11,22,3,44,5,4,3,33,11,12,11,43], 6),
        ([1,1,1,3,4,5,5,8,1,8,9], 6),
    ]

    for test in test_list:
        ans = estetic(test[0], test[1])
        print(f"(vitrine 1, vitrine 2) = {ans}")


if __name__ == "__main__":
     main()
'''
Author: Ahmed Guetti
Atelir: 2
date: 09/09/2023

exercice 5
'''

def estetic (obj:list, nbEmplacement:int)->tuple:
    """
    une fonction qui simule un exemple réel d'un algorithme
    exemple:
        input:  objs:=[1,2,2,3,4,5,5], nbEmplacement:=4
        output: ([1,2,3,5], [2,4,5])
    Args:
        obj (list): list des Oject, element quelconque pour le stocker dans les deux vitrines
        nbEmplacement (int): nombre des place disponible dans chaque vitrine

    Returns:
        tuple: un tuple de deux list qui represent les deux vitrines 
    """
    obj.sort()
    vitrine_1 = [[], nbEmplacement]
    vitrine_2 = [[], nbEmplacement]
    trash = []
    # check = False
    i=0
    while i < len(obj)-1 and (vitrine_1[1] > 0 and vitrine_2[1] > 0):
        if obj[i-1] == obj[i]:
             trash.append(obj[i])
             i+=1
             continue
        if obj[i] == obj[i+1]:
                vitrine_1[0].append(obj[i])
                vitrine_2[0].append(obj[i])
                vitrine_1[1] -= 1
                vitrine_2[1] -= 1
                i+=2
        else:
            if vitrine_1[1]  >= vitrine_2[1] or (vitrine_1[1]>0 and vitrine_2[1]<=0):
                vitrine_1[0].append(obj[i])
                vitrine_1[1] -= 1
            # elif vitrine_2[1]  >= vitrine_1[1] or (vitrine_2[1]>0 and vitrine_1[1]<=0):
            else:
                vitrine_2[0].append(obj[i])
                vitrine_2[1] -= 1
            i+=1
    if trash:
         print(f"[IMPOSSIBLE] TRASH: {trash}", end=" ") 
    return(vitrine_1[0], vitrine_2[0])







def main():
    """
    la fonction main qui sera notre point d'enter pour tester tous les cas possible
    """
    test_list = [
        ([1,2,2,3,4,5,5],4),
        ([],5),
        ([2,2,2,2,2,2,2], 5),
        ([1,2,4,4,5,6,7], 3),
        ([11,22,3,44,5,4,3,33,11,12,11,43], 6),
        ([1,1,1,3,4,5,5,8,1,8,9], 6),
    ]

    for test in test_list:
        ans = estetic(test[0], test[1])
        print(f"(vitrine 1, vitrine 2) = {ans}")


if __name__ == "__main__":
     main()
