VALID_MSG = "[VALIDE]   Cette date est valid"
WRONG_MSG = "[WRONG]    Cette date n'est pas valid"

def est_bissextile (year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0 )or year % 400 == 0 

def date_est_valide(jour:int,mois:int,annee:int)->bool:
    if (mois > 12 or mois < 0) or (mois % 2 == 1 and jour > 31) or (mois % 2 == 0 and jour > 30):
        return WRONG_MSG
    elif mois == 2:
        if (not (est_bissextile(annee)) and jour > 28) or (est_bissextile(annee) and jour > 29):
            return WRONG_MSG
        else:
            return VALID_MSG
    else :
        return VALID_MSG

def func_test ():
    print("12,5,2006", end=" -------> ")
    print(date_est_valide(12,5,2006))
    print("14,12,2035", end=" -------> ")
    print(date_est_valide(14,12,2035))
    print("14,15,2005", end=" -------> ")
    print(date_est_valide(14,15,2005))
    print("30,2,2021", end=" -------> ")
    print(date_est_valide(30,2,2021))
    print("28,2,2020", end=" -------> ")
    print(date_est_valide(28,2,2020))

func_test()