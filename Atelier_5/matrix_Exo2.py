import numpy as np

def make_matrix():
    """
    Crée une matrice aléatoire de dimensions 4x4 et une matrice identité de dimensions 4x4.

    Returns:
        None
    """
    print("_______  Crée une Matrice de valeurs aléatoires de 4x4  _______")
    x = np.random.randint(10, size=(4, 4))
    print(x)

    print("_______  Crée une matrice identité I de dimensions 4x4  _______")
    I = np.identity(4, dtype=int)
    print(I)

def matrice_trace(matrice: np.ndarray) -> int:
    """
    Calcule la trace d'une matrice carrée.

    Args:
        matrice (np.ndarray): La matrice carrée.

    Returns:
        int: La valeur de la trace.
    """
    diag = matrice.diagonal()
    ans = np.sum(diag)
    return ans

def matrice_traceV2(matrice: np.ndarray) -> int:
    """
    Calcule la trace d'une matrice carrée en utilisant la fonction `np.trace`.

    Args:
        matrice (np.ndarray): La matrice carrée.

    Returns:
        int: La valeur de la trace.
    """
    return np.trace(matrice)

def est_symetrique(matrice: np.ndarray) -> bool:
    """
    Vérifie si une matrice est symétrique.

    Args:
        matrice (np.ndarray): La matrice à vérifier.

    Returns:
        bool: True si la matrice est symétrique, False sinon.
    """
    return (np.transpose(matrice) == matrice).all()

def produit_diagonal(matrice: np.ndarray) -> int:
    """
    Calcule le produit des éléments de la diagonale d'une matrice.

    Args:
        matrice (np.ndarray): La matrice.

    Returns:
        int: Le produit des éléments de la diagonale.
    """
    return np.prod(np.diagonal(matrice))

def test_unit():
    """
    Fonction de test unitaire pour les fonctions principales.

    Returns:
        None
    """
    make_matrix()
    x = np.random.randint(10, size=(4, 4))

    trace = matrice_trace(np.identity(4))
    print(f"trace du matrice est : {trace}")

    print(f"x :\n {x}")
    res = est_symetrique(x)
    print(f"est_symetric(x) = {res}")

    res = produit_diagonal(x)
    print(f"produit_diagonal(x) = {res}")

def main():
    test_unit()

if __name__ == "__main__":
    main()
