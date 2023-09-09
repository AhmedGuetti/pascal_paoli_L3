'''
Author: Ahmed Guetti
Atelir: 2
date: 08/09/2023

exercice 4
'''
import matplotlib.pyplot as plt

def histo(F:list)->list:
    """ 
    histo: Histogram d'un fonction mathematique autrement dite une list du nombre de 
            repetition d'un element dans un list
    exemple:
        input:  L:=[6,5,6,7,4,2,1,5]  
        output: [0, 1, 1, 0, 1, 2, 2]

    Args:
        F (list): une list qui represent une fonction mathematique f(1) = F[1] et ainsi de suite

    Returns:
        list: une list qui resresent le histogram de F
    """
    H = [i for i in range(max(F))] # H represente le Histogramme de F
    for i in range(max(F)):
        count = 0
        for e in F:
            if i == e:
                count += 1
        H[i] = count
    return H


def est_injective(F:list)->bool:
    """
    test l'injectivite d'une fonction mathematique

    Args:
        F (list): une list qui represent une fonction mathematique f(1) = F[1] et ainsi de suite


    Returns:
        bool: return True si F est injective et Flase dans l'autre cas
    """
    H = histo(F)
    ans = True
    for e in H:
        if e > 1:
            ans = False
    return ans



def est_surjective(F:list)->bool:
    """
    test la surjectivite d'une fonction mathematique

    Args:
        F (list): une list qui represent une fonction mathematique f(1) = F[1] et ainsi de suite


    Returns:
        bool: return True si F est surjective et Flase dans l'autre cas
    """
    H = histo(F)
    ans = True
    for e in H:
        if e < 1:
            ans = False
    return ans



def est_bijective(F:list)->list:
    """
    test la bijectivite d'une fonction mathematique

    Args:
        F (list): une list qui represent une fonction mathematique f(1) = F[1] et ainsi de suite


    Returns:
        bool: return True si F est bijective et Flase dans l'autre cas
    """
    ans = False
    if est_injective(F) and est_surjective(F):
        ans = True
    return ans

def afficheHisto(F:list):
    """
    un fontion qui represente le Histograme dans un graphe utilisant les ASCII dans le terminal


    Args:
        F (list): une list qui represent une fonction mathematique f(1) = F[1] et ainsi de suite
    """
    H = histo(F)
    MAXOCC = max(H)

    i = MAXOCC
    while i > 0:
        for e in range(len(H)):
            if H[e] == 0 or H[e] < i:
                print("    ", end="")
            else:
                print(' #  ', end="")
        print("\n")
        i -= 1


    for i in range(max(F)):
        if i ==  max(F) -1:
            print("| --|", end="")
        else:
            print("| --", end="")
    print("\n")
    for i in range(max(F)):
        print(f"  {i} ", end ="")
    print("\n")
    


def afficheHisto_2(F:list):
    """
    une fonction comme afficheHisto mais il utilise un package pour le representer graphiquement 

    Args:
        F (list): une list qui represent une fonction mathematique f(1) = F[1] et ainsi de suite
    """
    plt.hist(F, edgecolor = 'red')
    plt.show()


def testing_fun(F:list):
    """
    une fonction pour afficher le type de fonction mathematique

    Args:
        F (list): une list qui represent une fonction mathematique f(1) = F[1] et ainsi de suite
    """
    if est_injective(F):
        print(f"F:={F} est injective")
    elif est_surjective(F):
        print(f"F:={F} est surjective")
    elif est_bijective(F):
        print(f"F:={F} est bijective")
    else:
        print(f"F:={F} n'a pas de type ")



def main():
    """
    la fonction main qui sera notre point d'enter pour tester tous les cas possible
    """
    F1=[6,5,6,7,4,2,1,5]
    H = histo(F1)
    print(H)
    testing_fun(F1)
    afficheHisto(F1)
    afficheHisto_2(F1)


if __name__ == "__main__":
    main()
