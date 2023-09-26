import numpy as np




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



def matriceIncidencev2(mat):
    n = len(mat)
    if n != len(mat[0]):
        return -1
    A = []
    for i in range(n):
        for j in range(n):
            if mat[i][j] == 1:
                A.append((i,j))

    m = len(A)
    incidence_matrix = np.zeros((n,m), dtype=int)
    for i,edge in enumerate(A):
        incidence_matrix[edge[0]][i] = 1
        incidence_matrix[edge[1]][i] = -1
    return incidence_matrix
    




def main():
    matAdj = matriceAdjacence([0,1,2,3,4], [(0,1), (0,2), (1,2), (1,4), (2,3), (3,4), (4,2)])
    # print(matriceAdjacencePond([1,2,3], [(0,1,3), (1,2,4), (2,0,10)]))
    # mat = lireMatriceFichier("file.mat")
    # print(f"the matrix is ---------------- \n {mat}")

    print(matriceIncidencev2(matAdj))

    

if __name__ == "__main__":
    main()
    