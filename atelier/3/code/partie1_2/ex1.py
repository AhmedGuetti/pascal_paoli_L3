
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
    ans[1] = ans[1].capitalize()
    return " ".join(ans)

def is_mail(str_arg:str)->tuple:
    if str_arg == '':
        response = (0,1)
    else:
            
        dot_exist = False
        response = (1,0)
        i = 0 
        # this part parse the cors of the main
        finish = True
        while str_arg[i] != '@' and finish:
            if i == 0 and str_arg[i] == '.':
                response = (0,1)
                finish = False
            elif i == len(str_arg)-1:
                response = (0,2)
                finish = False
                
            elif str_arg[i] == '.' and str_arg[i+1] == '.':
                response = (0,1)
                finish = False
                
            elif str_arg[i] == '.':
                dot_exist = True
            i+=1

            # this part check the near charactere of @
        if response == (1,0):
            if i == 0:
                response =  (0,1)
            elif str_arg[i-1] == '.':
                response =  (0,1)
            elif str_arg[i+1] == '.':
                response =  (0,3)

        # this part parse the domain of the email
        if response == (1,0):
            for j in range(i,len(str_arg)):
                if str_arg[j] == '.' and str_arg[j+1] == '.':
                    response =  (0,3)
                elif str_arg[i] == '.':
                    dot_exist = True
            
        # print(dot_exist)
        if str_arg.find('.') == -1:
            response = (0,4)

    return response
    


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
        'bisgambiglia_paul@univ-c..orse.fr',
        'bisgambiglia_paulOuniv-corse.fr',
        'bisgambiglia_paul@univ-corsePOINTfr',
        'bisgamb..iglia_paul@univ-corsePOINTfr',
        'bisgambiglia_paul@univ-corse..POINTfr',
        '',
        '@univ-corse.fr',
        '@univ-..corse.fr'
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
                
