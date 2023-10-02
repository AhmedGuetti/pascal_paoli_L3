import re 
def mots_Nlettres(lst_mot:list, n:int)->list:
    ans =[]
    for w in lst_mot:
        if len(w) == n:
            ans.append(w)
    return ans




def commence_par(mot:str, prefixe:str)->bool:
    return True if re.search(f"^{re.escape(prefixe)}.*", mot) else False


def finit_par(mot: str, suffixe: str) -> bool:
    return True if re.search(f".*{re.escape(suffixe)}$", mot) else False



def commence_par_v1(mot:str, prefixe:str)->bool:
    return True if mot.find(prefixe) == 0 else False

def finit_par_v1(mot:str, suffix:str)->bool:
    return True if len(mot) - mot.find(suffix) == len(suffix) else False



def commence_par_v2(mot:str, prefix:str)->bool:
    i = 0
    notfound = True
    w_lenght = len(prefix)
    ans  = True
    while i < w_lenght and notfound:
        if mot[i] != prefix[i]:
            ans  = False
            notfound = False
        i += 1
    return ans


def finit_par_v2(mot:str, suffix:str)->bool:
    ans = True
    if len(suffix) > len(mot):
        ans = False
    else:
        cond = True
        i = len(mot) - 1
        j = len(suffix) - 1
        while j >= 0 and cond:
            if mot[i] != suffix[j]:
                cond = False
            i -= 1
            j -= 1
    return ans




def finissent_par(lst_mot:list, suffixe:str)->list:
    ans = []
    for e in lst_mot:
        if finit_par(e,suffixe):
            ans.append(e)
    return ans

def commencent_par(lst_mot:list, prefixe:str)->list:
    ans = []
    for e in lst_mot:
        if commence_par(e, prefixe):
            ans.append(e)
    return ans


def finissent_par_v1(lst_mot:list, suffixe:str)->list:
    return list(filter(lambda mot: finissent_par(mot, suffixe), lst_mot))

def commencent_par_v1(lst_mot:list, prefixe:str)->list:
    return list(filter(lambda mot: commence_par(mot, prefixe), lst_mot))



def liste_mots (lst_mot:list, prefixe:str, suffixe:str, n:int)->list:
    return list(filter(lambda mot: finit_par(mot, suffixe) and commence_par(mot, prefixe) and len(mot) == n, lst_mot))





def liste_mots_v1(lst_mot:list, prefixe:str, suffixe:str, n:int)->list:
    
    s1 = set(finissent_par(lst_mot, suffixe))
    s2 = set(commencent_par(lst_mot, prefixe))
    s3 = set(mots_Nlettres(lst_mot, n))

    s_ans = s1.intersection(s2,s3)
    ans = list(s_ans)

    return ans



def dictionnaire(fichier:str)->list:
    ans = []
    f=open(fichier,"r")
    c=f.readline() 

    while c!="" :
        ans.append(c[:-1])
        c=f.readline()
    return ans






def testing_unit():
    """
        une fontion pour regrouper tous les test 
    """
   
    print("____________ Question 1 ____________")

    st_mot=["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour",
    "finir", "aimer"]
    ans = mots_Nlettres(st_mot, 5)
    print(f"ans = {ans}")

    print("____________ Question 2 ____________")

    for w in st_mot:
        ans0 = commence_par(w, "aur")
        ans1 = commence_par_v1(w, "aur")
        ans2 = commence_par_v2(w, "aur")

        if ans0:
            print(f"[VERSION 0] {w} commence par 'aur'")
             

        if ans1:
            print(f"[VERSION 1] {w} commence par 'aur'")
             

        if ans2:
            print(f"[VERSION 2] {w} commence par 'aur'")


    print("____________ Question 3 ____________")

    for w in st_mot:
        ans0 = finit_par(w, "ir")
        ans1 = finit_par_v1(w, "ir")
        
        if ans0:
            print(f"[VERSION 0] {w} fini par 'ir'") 

        if ans1:
            print(f"[VERSION 1] {w} fini par 'ir'") 

    
    print("____________ Question 6 ____________")

    ans0 = liste_mots(st_mot, "p","ir",5)
    ans1 = liste_mots_v1(st_mot, "p","ir",5)
    print(f"[VERSION 0] {ans0}")
    print(f"[VERSION 1] {ans1}")
    
    print("____________ Question 7 ____________")

    ans = dictionnaire("dict.txt")
    print(f"[dict.txt]  {ans}")






def main():
    """
    la fonction main qui sera notre point d'enter pour tester tous les cas possible
    """
    testing_unit()

if __name__ == "__main__":
    main()
                

