import numpy as np


def make_matrix():
    print("_______  Cree une Matrice des valeur aleatoire de 4x4  _______")
    x = np.random.randint(10, size=(4, 4))
    print(x)

    print("_______  Créez une matrice identité I de dimensions 4x4  _______")
    I = np.identity(4, dtype=int)
    print(I)


def matrice_trace(matrice:np.ndarray):
    diag = matrice.diagonal()
    ans = np.sum(diag)
    return ans


def matrice_traceV2(matrice:np.ndarray):
    return np.trace(matrice)


def est_symetrique(matrice: np.ndarray) -> bool:
    return (np.transpose(matrice) == matrice).all()





def produit_diagonal(matrice:np.ndarray):
    return np.prod(np.diagonal(matrice))



def test_unit():
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