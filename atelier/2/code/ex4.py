import ex1 as func
import matplotlib.pyplot as plt

def histo(F:list)->list:
    """
        complexity : O(n²)
        can be reduced using a hash map
    """
    H = [i for i in range(max(F))] # H represente le Histogramme de F
    for i in range(max(F)):
        count = 0
        for j in F:
            if i == j:
                count += 1
        H[i] = count
    return H


def est_injective(F:list)->bool:
    H = histo(F)
    ans = True
    for e in H:
        if e > 1:
            ans = False
    return ans



def est_surjective(F:list)->bool:
    H = histo(F)
    ans = True
    for e in H:
        if e < 1:
            ans = False
    return ans



def est_bijective(F:list)->list:
    ans = False
    if est_injective(F) and est_surjective(F):
        ans = True
    return ans

def afficheHisto(F:list):
    H = histo(F)
    MAXOCC = max(H)

    i = MAXOCC
    while i > 0:
        for e in range(len(H)):
            if H[e] == 0 or H[e] < i:
                print("    ", end="")
            else:
                print(' #  ', end="")
        print("\n")
        i -= 1


    for i in range(max(F)):
        if i ==  max(F) -1:
            print("| --|", end="")
        else:
            print("| --", end="")
    print("\n")
    for i in range(max(F)):
        print(f"  {i} ", end ="")
    print("\n")
    


def afficheHisto_2(F:list):
    plt.hist(F, edgecolor = 'red')
    plt.show()

F1=[6,5,6,7,4,2,1,5]
H = histo(F1)
print(H)
afficheHisto_2(F1)


