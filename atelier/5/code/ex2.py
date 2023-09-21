def Longeur (L:list):
    if not L:
        return 0
    return 1+Longeur(L[1:])


def findMin(L:list):
    if not L:
        raise Exception("[ERROR]: array must not be empty !!")
    if len(L) == 1:
        return L[0]
    return L[len(L)-1] if L[len(L)-1] < findMin(L[:-1]) else findMin(L[:-1])  
    


def ListPairs(L:list, Ltemp = [])->list:
    if not L:
        return Ltemp
    if L[-1] % 2 == 0:
        Ltemp.append(L[-1])
    return ListPairs(L[:-1], Ltemp)


def concat_list(L:list, concat = []):
    if not L:
        return concat
    


    
    


def main():
    L = [12,3,4,5,1,-88]
    min = findMin(L)
    long = Longeur(L)
    paire = ListPairs(L)
    print(min)
    print(long)
    print(paire)

if __name__ == "__main__":
    main()
