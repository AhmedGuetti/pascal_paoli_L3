import random
import math as m

def gen_list_random_int(int_nbr=10, int_binf=0, int_bsub=10) -> list:
    """
    Génère une liste de nombres entiers aléatoires.

    Args:
        int_nbr (int): Le nombre d'entiers à générer.
        int_binf (int): La borne inférieure pour les entiers générés.
        int_bsub (int): La borne supérieure pour les entiers générés.

    Returns:
        list: Une liste d'entiers aléatoires.
    """
    return [m.floor((random.random() * (int_bsub - int_binf + 1)) + int_binf) for e in range(int_nbr)]

def mix_list(list_to_mix: list) -> list:
    """
    Mélange aléatoirement les éléments d'une liste.

    Args:
        list_to_mix (list): La liste à mélanger.

    Returns:
        list: Une nouvelle liste avec les éléments mélangés.
    """
    L = list(list_to_mix)
    for i in range(1, len(L)):
        j = random.randint(0, i)
        L[i], L[j] = L[j], L[i]
    return L

def mix_list_v2(list_to_mix: list) -> list:
    """
    Mélange aléatoirement les éléments d'une liste sans répétition.

    Args:
        list_to_mix (list): La liste à mélanger.

    Returns:
        list: Une nouvelle liste avec les éléments mélangés.
    """
    ans = []
    fin = False
    i = 0
    while not fin:
        j = m.floor(random.random() * (len(list_to_mix)))
        if list_to_mix[j] is not None:
            ans.append(list_to_mix[j])
            list_to_mix[j] = None
            i += 1
        if i == len(list_to_mix):
            fin = True
    return ans

def choose_element_list(list_in_which_to_choose: list):
    """
    Choisis un élément aléatoire dans une liste.

    Args:
        list_in_which_to_choose (list): La liste à partir de laquelle choisir.

    Returns:
        object: L'élément choisi.
    """
    return list_in_which_to_choose[random.randint(0, len(list_in_which_to_choose) - 1)] if len(list_in_which_to_choose) != 0 else None

def extract_elements_list(list_in_which_to_choose: list, int_nbr_of_element_to_extract: int) -> list:
    """
    Extrait un certain nombre d'éléments aléatoires d'une liste.

    Args:
        list_in_which_to_choose (list): La liste à partir de laquelle extraire.
        int_nbr_of_element_to_extract (int): Le nombre d'éléments à extraire.

    Returns:
        list: Une liste des éléments extraits.
    """
    ans = []
    if int_nbr_of_element_to_extract > len(list_in_which_to_choose):
        ans = list_in_which_to_choose
    else:
        L = list(list_in_which_to_choose)
        for i in range(int_nbr_of_element_to_extract):
            ran_index = random.randint(0, len(L) - 1)
            elem = L.pop(ran_index)
            ans.append(elem)
    return ans

def extract_elements_list_v1(lst: list, k: int) -> list:
    """
    Extrait k éléments aléatoires d'une liste sans répétition.

    Args:
        lst (list): La liste à partir de laquelle extraire.
        k (int): Le nombre d'éléments à extraire.

    Returns:
        list: Une liste des éléments extraits.
    """
    n = len(lst)
    result = [None] * k
    pool = list(lst)
    for i in range(k):
        j = random.randint(0, n - i - 1)
        result[i] = pool[j]
        pool[j] = pool[n - i - 1]
    return result

def extract_elements_list_v2(lst: list, k: int) -> list:
    """
    Extrait k éléments aléatoires d'une liste sans répétition (version 2).

    Args:
        lst (list): La liste à partir de laquelle extraire.
        k (int): Le nombre d'éléments à extraire.

    Returns:
        list: Une liste des éléments extraits.
    """
    n = len(lst)
    result = [None] * k
    selected = set()
    for i in range(k):
        j = random.randint(0, n - 1)
        while j in selected:
            j = random.randint(0, n - 1)
        selected.add(j)
        result[i] = lst[j]
    return result

def extract_elements_list_v3(lst: list, k: int) -> list:
    """
    Extrait k éléments aléatoires d'une liste avec répétition si la taille de la liste est suffisamment grande.

    Args:
        lst (list): La liste à partir de laquelle extraire.
        k (int): Le nombre d'éléments à extraire.

    Returns:
        list: Une liste des éléments extraits.
    """
    n = len(lst)
    result = [None] * k
    if n <= 10 * k:
        pool = list(lst)
        for i in range(k):
            j = random.randint(0, n - i - 1)
            result[i] = pool[j]
            pool[j] = pool[n - i - 1]
    else:
        selected = set()
        for i in range(k):
            j = random.randint(0, n - 1)
            while j in selected:
                j = random.randint(0, n - 1)
            selected.add(j)
            result[i] = lst[j]
    return result


def testing_unit():
    """
    Fonction de test unitaire pour les fonctions principales.

    Returns:
        None
    """
  

    l1 = ["Apple", "Asus", "Lenovo", "Dell", "MSI"]
    # print(gen_list_random_int(100, 12,43))
    # print(gen_list_random_int())
    print("LA LIST MIXEE")
    print(f"list de base = {l1} \n mix_list({l1}) = {mix_list(l1)} \n mix_list_v1({l1}) = {mix_list_v2(l1)}")
    lst_sorted=[i for i in range(10)]
    print(lst_sorted)
    print("Liste triée de départ",lst_sorted)
    mixed_list=mix_list(lst_sorted)
    print("Liste mélangée obtenue",mixed_list)
    print("Liste triée de départ après appel à mixList, elle doit être inchangée",lst_sorted)

    print("Exercice 3")
    # Test de votre code
    print('Liste triée de départ',lst_sorted)
    e1 = choose_element_list(lst_sorted)
    print('A la première exécution',e1,'a été sélectionné')
    e2 = choose_element_list(lst_sorted)
    print('A la deuxième exécution',e2,'a été sélectionné')
    assert e1 != e2
    print("Exercice 4")
    # Test de votre code
    print('Liste de départ',lst_sorted)
    sublist = extract_elements_list_v2(lst_sorted,5)
    print('La sous liste extraite est',sublist)
    print('Liste de départ après appel de la fonction est',lst_sorted)





def main():
    testing_unit()


if __name__ == "__main__":
    main()
