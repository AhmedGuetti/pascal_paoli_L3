import math

def discriminant(a:float ,b:float ,c:float )-> float:
    if a == 0:
        return None
    else:
        return pow(b,2)-4*a*c

def racine_unique(a:float, b:float)->float:
    if a == 0: 
        return None
    else:
        return (-1*b)/(2*a)

def racine_double(a:float ,b:float ,delta:float ,num:float) -> float:
    if a == 0: 
        return None
    else :
        if num == 1:
            ans = (-1*b+math.sqrt(delta))/(2*a)
        elif num == 2:
            ans = (-1*b-math.sqrt(delta))/(2*a)
        return ans

def str_equation(a:float ,b:float ,c:float )->str:
    eval = lambda i: ("+" if i > 0 else "") + str(i)
    if b == 0:
        if a == 1:
            if c == 0:
                return "x²=0"
            else:
                return f"x²{eval(c)}=0"
        elif a == -1:
            if c == 0:
                return "-x²=0"
            else:
                return f"-x²{eval(c)}=0"
        elif a == 0:
            if c == 0:
                return "[ERR] no equation"
            else:
                return f"{eval(c)}=0"
        else:
            if c == 0:
                return f"{eval(a)}x²=0"
            else:
                return f"{eval(a)}x²{eval(c)}=0"
    else:
        if a == 1:
            if c == 0:
                return f"x²{eval(b)}x=0"
            else:   
                return f"x²{eval(b)}x{eval(c)}=0"
        elif a == -1:            
            if c == 0:
                return f"-x²{eval(b)}x=0"
            else: 
                return f"-x²{eval(b)}x{eval(c)}=0"
        elif a == 0:            
            if c == 0:
                return f"{eval(b)}x=0"
            else: 
                return f"{eval(b)}x{eval(c)}=0"
        else:
            if c == 0:
                return f"{eval(a)}x²{eval(b)}x=0"
            else: 
                return f"{eval(a)}x²{eval(b)}x{eval(c)}=0"


def solution_equation(a:float ,b:float ,c:float)->str:
    print("Solution de l'equation", end =" ")
    print(str_equation(a,b,c))
    delta = discriminant(a,b,c)
    if delta == None:
        print("[ERR] a doit etre different de 0\n\n")
    elif delta < 0:
        print("Pas de racine réelle\n\n")
    elif delta == 0:
        print(f"Racine unique : x= {racine_unique(a,b)} \n\n")
    else:
        print(f"Deux racines :\n x1 = {racine_double(a,b, delta, 1)}\n x2 = {racine_double(a,b, delta, 2)}\n\n")


def funct_test ():
    solution_equation(1,0,1)
    solution_equation(-1,2,1)
    solution_equation(0,2,1)
    solution_equation(1,2,0)
    solution_equation(1,0,-4)
    solution_equation(2,-1,-6)


funct_test()
