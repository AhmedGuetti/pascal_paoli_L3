def Longeur(L: list) -> int:
    """
    Calcule la longueur d'une liste de manière récursive.

    Args:
        L (list): La liste dont on veut calculer la longueur.

    Returns:
        int: La longueur de la liste.
    """
    if not L:
        return 0
    return 1 + Longeur(L[1:])

def findMin(L: list) -> int:
    """
    Trouve le minimum d'une liste de manière récursive.

    Args:
        L (list): La liste dans laquelle on cherche le minimum.

    Returns:
        int: Le minimum de la liste.
    
    Raises:
        Exception: Si la liste est vide.
    """
    if L == []:
        raise Exception("[ERROR]: la liste ne doit pas être vide !!")
    if L[0] == L[-1]:
        return L[0]
    return L[len(L) - 1] if L[len(L) - 1] < findMin(L[:-1]) else findMin(L[:-1])

def ListPairs(L: list, Ltemp=[]) -> list:
    """
    Récupère les éléments pairs d'une liste de manière récursive.

    Args:
        L (list): La liste dont on veut extraire les éléments pairs.
        Ltemp (list): La liste temporaire pour stocker les éléments pairs.

    Returns:
        list: Une liste contenant les éléments pairs de la liste d'origine.
    """
    if not L:
        return Ltemp
    if L[-1] % 2 == 0:
        Ltemp.append(L[0])
    return ListPairs(L[1:], Ltemp)

def concat_list(L: list, concato=[]) -> list:
    """
    Concatène une liste de listes en une seule liste de manière récursive.

    Args:
        L (list): La liste de listes à concaténer.
        concato (list): La liste temporaire pour stocker les éléments concaténés.

    Returns:
        list: Une liste contenant tous les éléments des listes d'origine concaténés.
    """
    if not L:
        return concato
    else:
        concato += L[0]
    return concat_list(L[1:], concato)

def separe(L: list, res=([], [])) -> (list, list):
    """
    Sépare les éléments pairs et impairs d'une liste de manière récursive.

    Args:
        L (list): La liste à diviser en éléments pairs et impairs.
        res (tuple): Un tuple contenant deux listes, une pour les éléments pairs et une pour les impairs.

    Returns:
        tuple: Un tuple contenant deux listes, une pour les éléments pairs et une pour les impairs.
    """
    if not L:
        return res
    if L[0] % 2 == 0:
        res[0].append(L[0])
    else:
        res[1].append(L[0])
    return separe(L[1:], res)

def main():
    L = [12, 3, 4, 5, 1, -88]
    min = findMin(L)
    long = Longeur(L)
    paire = ListPairs(L)
    concat = concat_list([[0, 1], [2, 3], [4], [6, 7]])  # [0,1,2,3,4,6,7]
    sepa = separe([1, 20, 2, 4, 5])

    print("Minimum:", min)
    print("Longueur:", long)
    print("Éléments pairs:", paire)
    print("Concaténation de listes:", concat)
    print("Séparation des éléments pairs et impairs:", sepa)

if __name__ == "__main__":
    main()
