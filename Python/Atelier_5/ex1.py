def somme_recursive(L: list) -> int:
    """
    Calcule la somme des éléments d'une liste de manière récursive.

    Args:
        L (list): La liste d'entiers à additionner.

    Returns:
        int: La somme des éléments de la liste.
    """
    if len(L) == 0:
        return 0
    return L.pop() + somme_recursive(L)

def factorielle_recursive(nombre: int) -> int:
    """
    Calcule la factorielle d'un nombre de manière récursive.

    Args:
        nombre (int): Le nombre entier dont on veut calculer la factorielle.

    Returns:
        int: La factorielle du nombre.
    """
    if nombre == 0:
        return 1
    return nombre * factorielle_recursive(nombre - 1)

def main():
    res = somme_recursive([1, 2, 3, 4])
    print("Somme récursive:", res)

    res = factorielle_recursive(3)
    print("Factorielle récursive:", res)

if __name__ == "__main__":
    main()
