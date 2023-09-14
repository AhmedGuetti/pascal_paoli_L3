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
    ans = False
    i = len(mot) - 1
    j = len(suffix) - 1

    

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

    






def main():
    """
    la fonction main qui sera notre point d'enter pour tester tous les cas possible
    """
    testing_unit()

if __name__ == "__main__":
    main()
                

