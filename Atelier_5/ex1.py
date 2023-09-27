def somme_recursive(L:list): 
    if len(L) == 0:
        return 0
    return L.pop()+somme_recursive(L)


def factorielle_recursive(nombre:int):
    if nombre == 0:
        return 1
    return nombre * factorielle_recursive(nombre-1)




def main():
    res = somme_recursive([1,2,3,4])
    print(res)

    res = factorielle_recursive(3)
    print(res)

if __name__ == "__main__":
    main()



    
