import re

def full_name(str_arg:str)->str:
    """
    une fonction qui return le nom formatted d'une manier propre
    Args:
        str_arg (str): le nom et prenom "nome prenom"
    Returns:
        str: le nom et prenom en Majuscule (NOM Prenom)
    """
    ans = str_arg.split(" ")
    ans[0] = ans[0].upper()
    ans[1] = ans[1].lower().capitalize()
    return " ".join(ans)

def is_mail(str_arg:str)->(int, int):
    """
    une fontion qui check si une email est valid 
    
    usename@domain_name.domain
    username ---> can have [a-zA-Z0-9._-] multiple times 
    domain_name ----> can have [a-zA-Z0-9.-]
    domain ---> can have [a-zA-Z] multiple times

    ^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$

    Args:
        str_arg (str): _description_
        int (_type_): _description_
    """

    ans = (1,0)
    # pattern = r"^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]+$"
    # check = re.match(pattern, str_arg) 
    
    # if not check:
    #     ans = (0,1)
    # else:
    if not str_arg.find('@'):
        ans = (0,2)
    elif not str_arg.find('.'):
        ans = (0,4)
    else:
        if str_arg[0] != '@':
            ans = (0,1)
        else:
            username, domain = str_arg.split('@')
            two_point_username = any(True for i,j in zip(username, username[1:]) if i == j and i == '.')
            two_point_domain = any(True for i,j in zip(domain, domain[1:]) if i == j and i == '.')

            if two_point_username\
                or username[0] == '.' or username[-1] == '.':
                ans = (0,1)
            elif domain[0] == '.' \
                or domain[-1] == '.' \
                or not domain and two_point_domain:
                ans = (0,3)
            else:
                ans = (1,0)
    return ans 

def testing_unit():
    """
        une fontion pour regrouper tous les test 
    """
    print("Question 3 ".center(20,'_'))
    name  = full_name("Ahmed guetti")
    print(name)

    print("____________ Question 2 ____________")

    str_variable2test = [
        'bisgambiglia_paul@univ-corse.fr',
        'bisgambiglia_paulOuniv-corse.fr',
        'bisgambiglia_paul@univ-corsePOINTfr',
        '@univ-corse.fr'
    ]

    for str in str_variable2test:
        ans = is_mail(str)
        print(f"is_mail({str} ----> {ans})")
        # doit renvoyer (1,0)
        # doit renvoyer (0,2)
        # doit renvoyer (0,4)
        # doit renvoyer (0,1)



def main():
    """
    la fonction main qui sera notre point d'enter pour tester tous les cas possible
    """
    testing_unit()

if __name__ == "__main__":
    main()
