import numpy as np
import matrix_Exo2 as mtEx2


def matriceAdjacence(S:list,A:list)->np.ndarray:
    ans = np.zeros((len(S), len(S)), dtype=int)
    for arc in A:
        ans[arc[0]][arc[1]] = 1
    return ans

def matriceAdjacencePond(S:list,A:list)->np.ndarray:
    ans = np.zeros((len(S), len(S)), dtype=int)
    for arc in A:
        ans[arc[0]][arc[1]] = arc[2]
    return ans

def lireMatriceFichier(nomfichier:str)->np.ndarray:
    matrice = []
    fileMatrice = open(nomfichier, 'r')
    Lines = fileMatrice.readlines()
    
    for line in Lines:
        new_line = np.fromstring(line.strip(), dtype=int, sep=' ')
        print(new_line)
        matrice.append(new_line)
    matrice = np.array(matrice, dtype=int)
    return matrice



def lireMatriceFichier(nomfichier: str) -> np.ndarray:
    matrice = []  # Initialize as an empty list
    with open(nomfichier, 'r') as fileMatrice:
        for line in fileMatrice:
            new_line = np.fromstring(line.strip(), dtype=int, sep=' ')
            matrice.append(new_line)
    
    # Convert the list of lists to a NumPy array
    matrice = np.array(matrice, dtype=int)
    
    return matrice



def  tousLesSommets(mat:np.ndarray):
    return [i for i in range(len(mat))]

def  listeArcs(mat):
    A = []
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j] == 1:
                A.append((i,j))
    return A


def matriceIncidence(mat:np.ndarray)->np.ndarray:
    """
    Generate the incidence matrix of a graph represented by an adjacency matrix.

    Args:
        mat (np.ndarray): A square adjacency matrix representing the graph.

    Returns:
        np.ndarray or None: The incidence matrix of the graph, or None if the input matrix is not square.
    """

    n = len(mat)
    if n != len(mat[0]):
        return None
    
    A = listeArcs(mat)
    m = len(A)
    
    incidence_matrix = np.zeros((n,m), dtype=int)
    
    for i,edge in enumerate(A):
        incidence_matrix[edge[0]][i] = 1
        if not mtEx2.est_symetrique(mat):
            incidence_matrix[edge[1]][i] = -1
        else:
            incidence_matrix[edge[1]][i] = 1

    return incidence_matrix
    



# def matriceIncidence(mat: np.ndarray):
#     n, m = mat.shape[0], np.count_nonzero(mat == 1)
    
#     if n != mat.shape[1]:
#         return None
    
#     incidence_matrix = np.zeros((n, m), dtype=int)
    
#     is_symmetric = np.array_equal(mat, mat.T)  # Check if the matrix is symmetric
    
#     edge_index = 0
    
#     for i in range(n):
#         for j in range(i + 1, n):
#             if mat[i][j] == 1:
#                 incidence_matrix[i][edge_index] = 1
#                 incidence_matrix[j][edge_index] = -1 if not is_symmetric else 1
#                 edge_index += 1

#     return incidence_matrix





def main():
    matAdj = matriceAdjacence([0,1,2,3,4], [(0,1), (0,2), (1,2), (1,4), (2,3), (3,4), (4,2)])
    matAdj2 = matriceAdjacence([0,1,2,3,4], [(0,1),(1,0), (0,2),(2,0), (1,2),(2,1), (1,4),(4,1), (2,3),(3,2), (3,4),(4,3), (4,2),(2,4)])
    
    # print(matriceAdjacencePond([1,2,3], [(0,1,3), (1,2,4), (2,0,10)]))
    # mat = lireMatriceFichier("file.mat")
    # print(f"the matrix is ---------------- \n {mat}")

    mat = np.array([
        [0,1,1,1],
        [1,0,0,1],
        [1,0,0,1],
        [1,1,1,0]])
    print(matriceIncidence(matAdj))
    print(matriceIncidence(mat))

    

if __name__ == "__main__":
    main()
    