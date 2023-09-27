import random
import sys

def places_lettre(ch : str, mot : str) -> list:
    return [i for i,e in enumerate(mot) if e == ch]


def outputStr(mot:str, lpos:list)-> str:
    return ''.join([mot[i] if i in lpos else '-' for i in range(len(mot))])


def build_list(fileName : str) -> list:
    ans = []
    file = open(fileName, "r")
    content = file.readlines()
    for line in content:
        words = line.rstrip().split("\t")
        for word in words:
            ans.append(word)
    file.close()
    return ans 




def build_dict(lst: list) -> dict:
    ans = {}
    for i in range(len(lst)):
        size = len(lst[i])
        if size not in ans:
            ans[size] = []
        ans[size].append(lst[i])
    return ans



def select_word(sorted_words:dict, word_len:int)->str:
    return sorted_words[word_len][random.randint(0, len(sorted_words[word_len]))]






def runGame_v1():
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





# def runGame():

#     # • niveau ‘easy’   ==  1      taille du mot < 7
#     # • niveau ‘normal’ ==  2    6 < taille du mot < 9
#     # • niveau ‘hard’   ==  3      taille du mot > 8


#     country = build_dict(build_list("countries.txt"))
#     country_niv = {}

#     country_char_count = list(country.keys())
#     # lst_len = len(lst)
#     # mot = lst[random.randint(1, lst_len)]
#     tentatives = 0
#     lose = False
#     mot = "" 

#     while True:
#         niveux = input("Saisir une niveux de diffucilty [easy/ normal/ hard]\n")
#         if niveux == "easy":
#             l = rm.randint(0, len(country_char_count))
#             while country_char_count[l] > 7 and country_char_count[l] < 1:
#                 l = rm.randint(0, len(country_char_count))
#             mot = select_word(country, country_char_count[l])
#             break
            
#         elif niveux == "normal":
#             l = rm.randint(0, len(country_char_count))
#             while country_char_count[l] < 5 and country_char_count[l] > 10:
#                 l = rm.randint(0, len(country_char_count))
#             mot = select_word(country, country_char_count[l])
#             break

#         elif niveux == "hard":
#             l = rm.randint(0, len(country_char_count))
#             while country_char_count[l] < 7 and country_char_count[l] > country_char_count[-1]:
#                 l = rm.randint(0, len(country_char_count))
#             mot = select_word(country, country_char_count[l])
#             break

#     while tentatives < 5:
#         print(outputStr(mot, ans))
#         ch = input("Saisir une lettre\n")
#         place = places_lettre(ch, mot)
#         if place != []:
#             for m_i in places_lettre(ch, mot):
#                 ans.append(m_i)
#         else:
#             if tentatives == 0:
#                 lose = True
#             print(" ============= ")
#             if tentatives>2:
#                 print(" ||/       |  ")
#             elif tentatives>3:
#                 print(" ||        0  ")
#             elif tentatives>4:
#                 print(" ||       /|\ ")
#             elif tentatives>5:
#                 print(" ||       /|  ")
#             print("==============\n")
#             tentatives += 1
#     if lose:
#         print("YOU DIED !!")
#     else:
#         print("YOU WIN !!")


def runGame():

    country = build_dict(build_list("countries.txt"))
    country_char_count = list(country.keys())
    tentatives = 0
    lose = False
    ans = []
    mot = ""

    while True:
        niveux = input("Saisir une niveux de diffucilty [easy/ normal/ hard]\n")
        if niveux == "easy":
            l = random.randint(1, 7)
            while l not in country_char_count:
                l = random.randint(1, 7)
            mot = select_word(country, l) 
            break
        elif niveux == "normal":
            l = random.randint(6, 8)
            while l not in country_char_count:
                l = random.randint(6, 8)
            mot = select_word(country, l) 
            break
        elif niveux == "hard":
            l = random.randint(9, len(country_char_count))
            while l not in country_char_count:
                l = random.randint(9, len(country_char_count))
            mot = select_word(country, l) 
            break

    while tentatives < 6:
        print(outputStr(mot, ans))
        ch = input("Saisir une lettre\n")
        place = places_lettre(ch, mot)
        if place:
            for m_i in place:
                ans.append(m_i)
        else:
            if tentatives == 0:
                lose = True
            print(" ============= ")
            if tentatives >= 1:
                print(" ||/       |  ")
            if tentatives >= 2:
                print(" ||        0  ")
            if tentatives >= 3:
                print(" ||       /|\ ")
            if tentatives >= 4:
                print(" ||       /|  ")
            print("==============\n")
            tentatives += 1

        if all(ch in ans for ch in mot):
            break
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
    # print(outputStr('calan',[1,3])     )# -> '_ a _ a _'


    runGame()
    # d = build_dict(build_list("countries.txt"))
    # for keys,values in d.items():
    #     print(keys)
    #     print(values)

    # print(select_word(d, 8))


    # country = build_dict(build_list("countries.txt"))
    # country_char_count = list(country.keys())
    # print(country_char_count)
    # l = random.randint(1, 7)
    # print(l)
    # while l not in country_char_count:
    #     l = random.randint(1, 7)
    #     print(l)


def main():
    """
    la fonction main qui sera notre point d'enter pour tester tous les cas possible
    """
    testing_unit()



if __name__ == "__main__":
    main()
                

