import numpy as np


# exemple 1
print("______ EXEMPLE 1 ______")
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)


print("______ EXEMPLE 2 ______")
# exemple 2
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    for y in x:
        print(y)


print("______ EXEMPLE 3 ______")
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7)
print(x)



#Exemple d’usage de la fct where

print("______ EXEMPLE 4 ______")
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)


print("______ EXEMPLE 5: Addition des Matrices ______")

A = np.array(([3,1],[6,4]))
B = np.array(([1,8],[4,2]))
A.shape == B.shape
# true (vérification de la dimension)
R = A + B
print(R)


def my_searchsorted(table : object, element : int)-> int:
    l = len(table) 
    i = 0
    while i < l and table[i] != element:
        i += 1
    else:
        if table[i] != element:
            i = -1
    return i


def my_where(table : object, element : int )-> list:
    ans = list()
    for i,e in enumerate(table):
        if e == element:
            ans.append(i)
    return ans

def my_where_v2(table: object, e: int)->int:
    return [i for i,c in enumerate(table) if c == e ]


"""[
    [1,2,3]
    [3,4,5]
    [6,7,8]
]"""




def my_add(tableA : object, tableB : object)-> object:
    if len(tableA) != len(tableB):
        return None

    ans = list()
    row = list()
    for ra,rb in zip(tableA, tableB):
        if len(ra) != len(rb):
            return None
        for ca, cb in zip(ra, rb):
            row.append(ca+cb)
        ans.append(row)
        row = []
    return ans






def main():
    print("______ Question 1 ______")

    ans  = my_searchsorted([6, 7, 8, 9], 9)
    print(ans)
    print("______ Question 2 ______")

    ans1  = my_where([1, 2, 3, 4, 5, 4, 4],4)
    print(ans1)
    ans2  = my_where_v2([1, 2, 3, 4, 5, 4, 4],4)
    print(ans2)

    print("______ Question 3 ______")


    A = [[3,1],[6,4]]
    B = [[1,8],[4,2]]
    ans = my_add(A,B)
    print(ans)

    print("______ MATRIX ______")

    #Initialisation et affichage

    matr = np.arange(1,10, dtype=int).reshape((3, 3))
    print(matr)

    out1 = matr + 10
    print(f"output 1 matr+10 =\n {out1} ")

    out2 = matr * 2
    print(f"output 2 matr*2 =\n {out2} ")

    slice1 = matr[2]
    print(f"slice 1 row2 of mattr =\n {slice1} ")

    print(f"shape = {matr.shape}matr = \n {matr} ")

    slice2 = matr[:, 2]
    print(f"slice 2 col3 of mattr =\n {slice2} ")



    slice3 = matr[np.ix_([0,1],[0,1])]
    slice3v2 = matr[0:2, [0,1]]
    print(f"slice 3 [2x2] depuis la gauche of mattr =\n {slice3} ")
    print(f"[VERSION 2]slice 3 [2x2] depuis la gauche of mattr =\n {slice3v2} ")



    




if __name__ == "__main__":
    main()