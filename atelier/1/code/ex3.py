import math

def discriminant(a:float ,b:float ,c:float )-> float:
    if a != 0:
        return pow(b,2)-4*a*c
    return None
    
def racine_unique(a:float, b:float)->float:
    if a != 0:
        return (-1*b)/(2*a)
    return None
        

def racine_double(a:float ,b:float ,delta:float ,num:float) -> float:
    if a != 0: 
        if num == 1:
            ans = (-1*b+math.sqrt(delta))/(2*a)
        elif num == 2:
            ans = (-1*b-math.sqrt(delta))/(2*a)
        return ans
    return None
        

def str_equation(a:float ,b:float ,c:float )->str:
    eval = lambda i: ("+" if i > 0 else "") + str(i)
    elements = []
    if a != 0:
        if a == 1:
            elements.append("x²")
        elif a == -1:
            elements.append("-x²")
        else:
            elements.append(f"{a}x²")
    
    if b != 0:
        if b == 1:
            elements.append("x")
        elif b == -1:
            elements.append("-x") 
        else:
            elements.append(f"{eval(b)}x")
    if c != 0:
        elements.append(f"{eval(c)}")
    
    if not str_equation:
        return "[ERR] the folowing parameter doesn't make an equation"

    return "".join(elements) + " =0"

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
