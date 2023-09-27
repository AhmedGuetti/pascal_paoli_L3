#VERSION 1

# def present1 (L, e) :
#     for i in range (0, len(L), 1) :
#         if (L[i] == e) :
#             return(True)
#         else :
#             return (False)
#     return (False)


def present1 (L, e) :
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            return(True)
        # else :
        #     return (False)
    return (False)


#VERSION 2
# def present2 (L, e) :
#     b=True
#     for i in range (0, len(L), 1) :
#         if (L[i] == e) :
#             b=True
#         else :
#             b=False
#     return (b)
"""
______ VERSION 2 ______
ECHEC: test liste vide
ECHEC: test absence
SUCCES: test fin
ECHEC: test absence
ECHEC: test absence

"""


def present2 (L, e) :
    b=False # b=True
    for i in range (0, len(L), 1) :
        if L[i] == e :
            b=True
            # break (on laisse le else et ajoutons un break)
        # else:
        #     b=False
    return b


#VERSION 3
# def present3 (L, e) :
#     b=True
#     for i in range (0, len(L), 1) :
#         return (L[i] == e)

def present3 (L, e) :
    b=True
    for i in range (0, len(L), 1) :
        # return (L[i] == e)
        return any([x == e for x in L])
    

#VERSION 4
# def present4 (L, e) :
#     b=False
#     i=0
#     while (i<len(L) and b) :
#         if (L[i] == e) :
#             b=True
#     return (b)

def present4 (L, e) :
    b=False
    i=0
    while (i<len(L) and b) :
        if (L[i] == e) :
            b=True
        i += 1  # added 
    return (b)



# ==================================================================

#VERSION 1
def pos1(L, e) :
    Lres = list() #Lres 
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres += [i]
    return Lres


# VERSION 2
def pos2(L, e) :
    Lres = list()
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres.append(i)
    return Lres


# VERSION 3
def pos3(L, e) :
    Lres = []
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres.append(i)
    return Lres


# VERSION 4
def pos4(L, e) :
    nb= L.count(e)
    Lres = [0]*nb
    j=0
    for i in range (0, len(L), 1) :
        if (L[i] == e) :
            Lres[j]= i
            j+= 1
    return Lres