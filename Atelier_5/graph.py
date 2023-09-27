import numpy as np
import matrix_Exo2 as mtEx2

def matriceAdjacence(S: list, A: list) -> np.ndarray:
    """
    Crée une matrice d'adjacence à partir de listes de sommets et d'arcs.

    Args:
        S (list): Liste des sommets.
        A (list): Liste des arcs sous forme de tuples (sommet1, sommet2).

    Returns:
        np.ndarray: Matrice d'adjacence résultante.
    """
    ans = np.zeros((len(S), len(S)), dtype=int)
    for arc in A:
        ans[arc[0]][arc[1]] = 1
    return ans

def matriceAdjacencePond(S: list, A: list) -> np.ndarray:
    """
    Crée une matrice d'adjacence pondérée à partir de listes de sommets et d'arcs.

    Args:
        S (list): Liste des sommets.
        A (list): Liste des arcs sous forme de tuples (sommet1, sommet2, poids).

    Returns:
        np.ndarray: Matrice d'adjacence pondérée résultante.
    """
    ans = np.zeros((len(S), len(S)), dtype=int)
    for arc in A:
        ans[arc[0]][arc[1]] = arc[2]
    return ans

def lireMatriceFichier(nomfichier: str) -> np.ndarray:
    """
    Lit une matrice à partir d'un fichier texte et la renvoie sous forme de tableau NumPy.

    Args:
        nomfichier (str): Le nom du fichier à lire.

    Returns:
        np.ndarray: La matrice lue à partir du fichier.
    """
    matrice = []
    with open(nomfichier, 'r') as fileMatrice:
        for line in fileMatrice:
            new_line = np.fromstring(line.strip(), dtype=int, sep=' ')
            matrice.append(new_line)
    
    matrice = np.array(matrice, dtype=int)
    return matrice

def tousLesSommets(mat: np.ndarray):
    """
    Renvoie tous les sommets à partir d'une matrice d'adjacence.

    Args:
        mat (np.ndarray): Matrice d'adjacence.

    Returns:
        list: Liste de tous les sommets.
    """
    return [i for i in range(len(mat))]

def listeArcs(mat):
    """
    Renvoie la liste des arcs à partir d'une matrice d'adjacence.

    Args:
        mat: Matrice d'adjacence.

    Returns:
        list: Liste des arcs sous forme de tuples (sommet1, sommet2).
    """
    A = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 1:
                A.append((i, j))
    return A

def matriceIncidence(mat: np.ndarray) -> np.ndarray:
    """
    Génère la matrice d'incidence d'un graphe représenté par une matrice d'adjacence.

    Args:
        mat (np.ndarray): Une matrice d'adjacence carrée représentant le graphe.

    Returns:
        np.ndarray or None: La matrice d'incidence du graphe, ou None si la matrice d'entrée n'est pas carrée.
    """
    n = len(mat)
    if n != len(mat[0]):
        return None
    
    A = listeArcs(mat)
    m = len(A)
    
    incidence_matrix = np.zeros((n, m), dtype=int)
    
    for i, edge in enumerate(A):
        incidence_matrix[edge[0]][i] = 1
        if not mtEx2.est_symetrique(mat):
            incidence_matrix[edge[1]][i] = -1
        else:
            incidence_matrix[edge[1]][i] = 1

    return incidence_matrix

def main():
    print("Testing Unit")

if __name__ == "__main__":
    main()
