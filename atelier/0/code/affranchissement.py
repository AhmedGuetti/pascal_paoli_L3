import re
import math
# LETTER_TYPE = ["LETTRE VERTE", "LETTRE PRIORITAIRE", "ECOPLI", "COLISSIMO ECO OUTREMER", "CÉCOGRAMME"]
ZONE_OM1 = ["Guyane", "Guadeloupe", "Martinique", "La Réunion", "St Pierre et Miquelon", "St Barthélémy", "St-Martin et Mayotte"]
ZONE_OM2 = ["Nouvelle-Calédonie", "Polynésie française", "Wallis-et-Futuna","T.A.A.F."]
WEIGHT_PATTERN = r'(\d+\s*)(kg|g)'
TARRIF = {
    "LV" : {
        20: 1.16,
        100: 2.32,
        250:  4.0,
        500: 6.0,
        1000: 7.5,
        3000: 10.50
    },
    "LP":{
        20: 1.43,
        100: 2.86,
        250:  5.26,
        500: 7.89,
        3000: 11.44
    },
    "ECOPLI":{
        20: 1.14,
        100:2.28,
        250:3.92
    },
}

def get_close_value(weight:int, letter_type:str)->tuple:
    poids = list(TARRIF[letter_type].keys())
    ans = None
    for poid in poids:
        if poid >= weight:
            ans = poid
            break
    if ans == None:
        return poids[-1]
    else:
        return (ans, TARRIF[letter_type][ans])

def parse_weight(weight:str):
    match_poids = re.search(WEIGHT_PATTERN, weight, re.IGNORECASE)
    if not match_poids:
        print("Please enter un poids valid number(kg) or (g) example: 12kg, 500g")
        while not match_poids:
            match_poids = re.search(WEIGHT_PATTERN, weight, re.IGNORECASE)
    poids = int(match_poids.group(1))
    units = match_poids.group(2)
    if units.lower() == 'kg':
        poids = poids * 100
    return poids



def get_info ()->dict:
    letter_type = ''
    zone = ''
    stiker = False
    poids = 0
    letter_type = input("LETTRE VERTE ---> LV\nLETTRE PRIORITAIRE ---> LP\nECOPLI ---> ECOPOLI\n")
    i = 0
    while i < min(len(ZONE_OM1), len(ZONE_OM2)):
        print(f"ZONE_OM1: {ZONE_OM1[i]} | ZONE_OM2: {ZONE_OM2[i]}")
        i+=1
    for j in range(i, max(len(ZONE_OM1), len(ZONE_OM2))):
        if max(len(ZONE_OM1), len(ZONE_OM2)) == len(ZONE_OM1):
            print(f"ZONE_OM1: {ZONE_OM1[j]}")
        else:
            print(f"ZONE_OM1: {ZONE_OM2[j]}")


    zone = input("Selectionee OM1 | OM2 \n")
    if letter_type in ['LV','LP','ECOPOLI']:
        ans =  input("Est-ce que vous avez un stiker ? Y/N ").upper()
        while ans != 'Y' and ans != "N":
            ans =  input("Est-ce que vous avez un stiker ? Y/N ").upper()
        if ans == 'Y':
            stiker == True
    poids_str = input("Entrer le poids de votre lettre en (g) ou (kg)")
    poids = parse_weight(poids_str)
    return {
        "letter_type"   : letter_type,
        "zone"          : zone,
        "poids"         : poids,
        "stiker"        : stiker
    }
def main():
    info = get_info()
    poids = info['poids']
    letter_type = info["letter_type"]
    stiker = info['stiker']
    zone = info['zone']
    ans = 0
    poids_devided_10 =  math.ceil(poids/10)
    if stiker:
            ans += 0.5
    if letter_type in ['LV', 'LP']:
        if zone.upper() == 'OM1':
            ans += poids_devided_10*0.05
        else:
            ans += poids_devided_10*0.11
    elif letter_type == 'ECOPLI':
        if zone.upper() == 'OM1':
            ans += poids_devided_10*0.02
        else:
            ans += poids_devided_10*0.05
    ans += get_close_value(poids, letter_type)[1]
    print(f" le montant de l’affranchissement:  {ans}€")


main()




