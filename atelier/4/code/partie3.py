import random as rm


def sort_list(listo:list)->list:
    # Bubble sort
    L = list(listo)
    for i in range(len(L)):
        for j in range(len(L) - i - 1):
            if L[j] > L[j+1]:
                L[j], L[j+1] =L[j+1], L[j]
    return L 




def tmp_moy(sort:callable, listo:list)->list:
    




def test_unit():
    


def main():
    test_unit()


if __name__ == "__main__":
    main()