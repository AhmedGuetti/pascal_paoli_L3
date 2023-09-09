# import random
import ex6_version as ver

def present(L:list,e:int)->bool:
    ans = False
    for entety in L:
        if entety == e:
            ans = True
            break
    return ans

def test_present(present:callable):
    searched = [25,45,44,89]
    ans = present([],searched[0])
    if ans:
        print("ECHEC: test liste vide")
    # list_test = [random.randint(0,100) for e in range(0,100)]
    # list_test = random.sample(range(0, 100), 10)
    list_test = [89, 44, 80, 21, 33, 2, 74, 65, 48, 45]
    for s in searched:
        ans = present(list_test, s)
        if not ans:
            print("SUCCES: test absence")
        else:
            print("ECHEC: test liste vide")
            print("SUCCES: test", end=" ")
            if list_test.index(s) == 0:
                print("debut")
            elif list_test.index(s) == len(list_test)-1:
                print("fin")
            else:
                print("milieu")




def pos(L:list, e:int)->list:
    ans = []
    for i in range(0,len(L)):
        if L[i] == e:
            ans.append(i)
    return ans


def test_pos(fonctionPos:callable):
    searched = [25,45,44,89]
    ans = present([],searched[0])
    if ans:
        print("ECHEC: test liste vide")
    else:
        print("SUCCES : test liste vide")


    # list_test = [random.randint(0,100) for e in range(0,100)]
    # list_test = random.sample(range(0, 100), 10)
    list_test = [89, 44, 80, 21, 33, 2, 74, 65, 48, 45, 15,55,48,3,54,21,44,33]
    print("\nECHEC: test liste vide")
    if not ans:
        print("SUCCES: test absence")
    else:
        print(f"SUCCES: test {ans}")
        # print("-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -", ) 
    for s in searched:
        ans = fonctionPos(list_test, s)
        print("\nECHEC: test liste vide")
        print(f"The searched value is = {s}")
        if not ans:
            print("SUCCES: test absence")
        else:
            print(f"SUCCES: test {ans}")
        
        # print("-   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -", ) 

    





def main():
    print(" =============== PRESENT =============== ")
    print("______ VERSION 0 ______")
    test_present(present)

    print("\n______ VERSION 1 ______")
    test_present(ver.present1)

    print("\n______ VERSION 2 ______")
    test_present(ver.present2)

    print("\n______ VERSION 3 ______")
    test_present(ver.present3)

    print("\n______ VERSION 4 ______")
    test_present(ver.present4)


    print(" =============== POSITION =============== ")
    print("______ VERSION 0 ______")
    test_pos(pos)

    print("\n______ VERSION 1 ______")
    test_pos(ver.pos1)

    print("\n______ VERSION 2 ______")
    test_pos(ver.pos2)

    print("\n______ VERSION 3 ______")
    test_pos(ver.pos3)

    print("\n______ VERSION 4 ______")
    test_pos(ver.pos4)








if __name__ == "__main__":
    main()



    
