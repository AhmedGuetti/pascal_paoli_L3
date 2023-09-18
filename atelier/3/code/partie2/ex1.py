import random


def places_lettre(ch : str, mot : str) -> list:
    return [i for i,e in enumerate(mot) if e == ch]


def outputStr(mot:str, lpos:list)-> str:
    return ''.join([mot[i] if i in lpos else '-' for i in range(len(mot))])


def runGame():
    lst =['paris','londres','madrid','berlin','new-york']

    lst_len = len(lst)
    mot = lst[random.randint(1, lst_len)]
    tentatives = 0
    ans = []
    lose = False
    while tentatives < 5:
        print(outputStr(mot, ans))
        ch = input("Saisir une lettre\n")
        place = places_lettre(ch, mot)
        if place != []:
            for m_i in places_lettre(ch, mot):
                ans.append(m_i)
        else:
            if tentatives == 0:
                lose = True
            print(" ==========Y= ")
            if tentatives>=1:
                print(" ||/       |  ")
            if tentatives>=2:
                print(" ||        0  ")
            if tentatives>=3:
                print(" ||       /|\ ")
            if tentatives>=4:
                print(" ||       /|  ")
            print("==============\n")
            tentatives += 1
    if lose:
        print("YOU DIED !!")
    else:
        print("YOU WIN !!")




def testing_unit():
    """
        une fontion pour regrouper tous les test 
    """
    
    print("____________ Question 1 ____________")

    # mot = input("Entrer un mot\n")
    # let = input("Entrer une lettre\n")

    # print(places_lettre(let, mot))
    # print(outputStr('bonjour',[])     )# -> '_ _ _ _ _ _ _'
    # print(outputStr('bonjour',[0])    )# -> 'b _ _ _ _ _ _'
    # print(outputStr('bonjour',[0,1,4]))# -> 'b o _ _ o _ _'
    # print(outputStr('bon',[0,1,2])    )# -> 'b o n'
    # print(outputStr('maman',[1,3])     )# -> '_ a _ a _'


    runGame()




def main():
    """
    la fonction main qui sera notre point d'enter pour tester tous les cas possible
    """
    testing_unit()



if __name__ == "__main__":
    main()
                

