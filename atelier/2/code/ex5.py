'''
Author: Ahmed Guetti
Atelir: 2
date: 09/09/2023

exercice 5
'''
def estetic (Object:list, nbEmplacement:int)->tuple:
    """
    une fonction qui simule un exemple réel d'un algorithme
    exemple:
        input:  Objects:=[1,2,2,3,4,5,5], nbEmplacement:=4
        output: ([1,2,3,5], [2,4,5])
    Args:
        Object (list): list des Oject, element quelconque pour le stocker dans les deux vitrines
        nbEmplacement (int): nombre des place disponible dans chaque vitrine

    Returns:
        tuple: un tuple de deux list qui represent les deux vitrines 
    """
    Object.sort()
    vitrine_1 = [[], nbEmplacement]
    vitrine_2 = [[], nbEmplacement]
    # check = False
    i=0
    while i < len(Object)-1 and (vitrine_1[1] > 0 and vitrine_2[1] > 0):
        if Object[i] == Object[i+1]:
                vitrine_1[0].append(Object[i])
                vitrine_2[0].append(Object[i])
                vitrine_1[1] -= 1
                vitrine_2[1] -= 1
                i+=2
        else:
            if vitrine_1[1]  >= vitrine_2[1] or (vitrine_1[1]>0 and vitrine_2[1]<=0):
                vitrine_1[0].append(Object[i])
                vitrine_1[1] -= 1
            # elif vitrine_2[1]  >= vitrine_1[1] or (vitrine_2[1]>0 and vitrine_1[1]<=0):
            else:
                vitrine_2[0].append(Object[i])
                vitrine_2[1] -= 1
            i+=1
    return(vitrine_1[0], vitrine_2[0])


def main():
    """
    la fonction main qui sera notre point d'enter pour tester tous les cas possible
    """
    ans = ()
    ans = estetic([1,2,2,3,4,5,5],4)
    print(ans)


if __name__ == "__main__":
     main()