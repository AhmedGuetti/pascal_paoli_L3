def message_imc (imc: float) -> str:
    str = ''
    if imc <= 16.5 and imc > 0:
        str = "dénutrition ou famine"
    elif imc <= 18.5:
        str = "maigreur"
    elif imc <= 25:
        str = "corpulence normale"
    elif imc <= 30:
        str = "surpoids"
    elif imc <= 35:
        str = "obésité modérée"
    elif imc <= 40:
        str = "obésité sévère"
    elif imc > 40:
        str = "obésité morbide"
    else:
        str = "imc doit etre superieure a 0"
    return str






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