def Longeur (L:list):
    if not L:
        return 0
    return 1+Longeur(L[1:])


def findMin(L:list):
    if L==[]:
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


def concat_list(L:list, concato = []):
    if not L:
        return concato
    if len(L) == 1:
        
        return  concato.extend(L[0])
    return concat_list(L[:-1], concato.extend(L[-1]))



def main():
    L = [12,3,4,5,1,-88]
    min = findMin(L)
    long = Longeur(L)
    paire = ListPairs(L)
    concat = [[0,1],[2,3],[4],[6,7]]

    

    print(min)
    print(long)
    print(paire)
    print(concat)

if __name__ == "__main__":
    main()
