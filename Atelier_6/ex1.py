def listeMultiples(binf:int,bsup:int,nb:int):
    return [i for i in range(binf, bsup) if i % nb == 0]

def ajouter(lst:list,nb:int)->list:
    return [lst[i]+nb for i in lst]

def ajouterSiSup(lst:list,val:int,nb:int)->list:
    return [lst[i]+nb for i in lst if val < lst[i]]

def bissextiles(adeb:int,afin:int):
    # Principe : une année bissextile est divisible par 4 et non par 100 ou par 400.
    return [i for i in range(adeb, afin+1) if (i % 4 == 0 and  i % 100!= 0) or i % 400!= 0]

def premiers(binf:int,bsup:int):
    return [i for i in range(binf+1, bsup) if  all([i%j != 0 for j in range(2, i-1)])]






def test_unit():
    p = premiers(10,100)
    print(p)

def main():
    test_unit()



if __name__ == "__main__" :
    main()
