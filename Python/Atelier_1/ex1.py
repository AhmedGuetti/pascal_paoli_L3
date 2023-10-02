# def message_imc (imc: float) -> str:
#     str = ''
#     if imc <= 16.5 and imc > 0:
#         str = "dénutrition ou famine"
#     elif imc <= 18.5:
#         str = "maigreur"
#     elif imc <= 25:
#         str = "corpulence normale"
#     elif imc <= 30:
#         str = "surpoids"
#     elif imc <= 35:
#         str = "obésité modérée"
#     elif imc <= 40:
#         str = "obésité sévère"
#     elif imc > 40:
#         str = "obésité morbide"
#     else:
#         str = "imc doit etre superieure a 0"
#     return str

DICT_IMC = {
    (0,16.5)            : "dénutrition ou famine",
    (16.5, 18.5)    : "maigreur",
    (18.5, 25)      : "corpulence normale",
    (25,   30)      : "surpoids",
    (30,   35)      : "obésité modérée",
    (35,   40)      : "obésité sévère",
    (40, float('inf'))              : "obésité morbide"
}

def message_imc (imc: int)->str:
    for (inf, sub), message in DICT_IMC.items():
        if inf <= imc and imc < sub:
            return message
    return "IMC doit etre superieur a 0"

def func_test ():
    message = ''
    values = [14, 17, 20, 24, 32, 37, 39, 55, -44]
    i = 0
    for imc in values:
        print(f"message number {i} for imc = {imc}", end=' ----> ')        
        message = message_imc(imc)
        print(message)
        i+=1 

func_test()
