def estetic (Object:list, nbEmplacement:int)->tuple:
    Object.sort()
    vitrine_1 = [[], nbEmplacement]
    vitrine_2 = [[], nbEmplacement]
    check = False
    i=0
    while i < len(Object)-1 and (vitrine_1[1] > 0 and vitrine_2[1] > 0):
        if Object[i] == Object[i+1]:
                vitrine_1[0].append(Object[i])
                vitrine_2[0].append(Object[i])
                vitrine_1[1] -= 1
                vitrine_2[1] -= 1
                i+=2
        else:
            if vitrine_1[1]  >= vitrine_2[1] or (vitrine_1[1]>0 and vitrine_2[1]<=0):
                vitrine_1[0].append(Object[i])
                vitrine_1[1] -= 1
            # elif vitrine_2[1]  >= vitrine_1[1] or (vitrine_2[1]>0 and vitrine_1[1]<=0):
            else:
                vitrine_2[0].append(Object[i])
                vitrine_2[1] -= 1
            i+=1
                

    return(vitrine_1[0], vitrine_2[0])


ans = ()
ans = estetic([1,2,2,3,4,5,5],4)
print(ans)


        
        
