import math

def discriminant(a:float ,b:float ,c:float )-> float:
    return pow(b,2)-4*a*c

def racine_unique(a:float, b:float)->float:
    if a == 0: 
        print("[ERR] a doit etre different de 0")
    else:
        return (-1*b)/(2*a)

def racine_double(a:float ,b:float ,delta:float ,num:float) -> float:
    if a == 0: 
        print("[ERR] a doit etre different de 0")
    else :
        if num == 1:
            ans = (-1*b+math.sqrt(delta))/(2*a)
        elif num == 2:
            ans = (-1*b-math.sqrt(delta))/(2*a)
        return ans

def str_equation(a:float ,b:float ,c:float )->str:
    #  ax2 +bx+c=0
    return str(a)+"x²+"+str(b)+"x+"+str(c)+"= 0"
def solution_equation(a:float ,b:float ,c:float)->str:
    print("Solution de l'equation", end =" ")
    print(str_equation(a,b,c))
    delta = discriminant(a,b,c)
    if delta < 0:
        print("Pas de racine réelle")
    elif delta == 0:
        print(f"Racine unique : x= {racine_unique(a,b)}")
    else:
        print(f"Deux racines :\n x1 = {racine_double(a,b, delta, 1)}\n x2 = {racine_double(a,b, delta, 2)}")


def funct_test ():
    solution_equation(1,2,1)


funct_test()