import random as rm

def sort_list(listo: list) -> list:
    """
    Trie une liste en utilisant l'algorithme de tri à bulles.

    Args:
        listo (list): La liste à trier.

    Returns:
        list: La liste triée.
    """
    L = list(listo)
    for i in range(len(L)):
        for j in range(len(L) - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L

def test_unit():
    """
    Teste la fonction de tri en utilisant des exemples.

    Returns:
        None
    """
    # Exemple 1 : Liste non triée
    unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = sort_list(unsorted_list)
    print("Exemple 1 - Liste non triée :")
    print("Entrée :", unsorted_list)
    print("Sortie triée :", sorted_list)

    # Exemple 2 : Liste déjà triée
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    unsorted_list = sort_list(sorted_list)
    print("\nExemple 2 - Liste déjà triée :")
    print("Entrée :", sorted_list)
    print("Sortie triée :", unsorted_list)

    # Exemple 3 : Liste vide
    empty_list = []
    sorted_list = sort_list(empty_list)
    print("\nExemple 3 - Liste vide :")
    print("Entrée :", empty_list)
    print("Sortie triée :", sorted_list)

if __name__ == "__main__":
    test_unit()
