from random import *
import math as m
def gen_list_random_int(int_nbr=10, int_binf=0, int_bsub=10)->list:
    return [m.floor((random()*(int_bsub-int_binf+1))+int_binf) for e in range(int_nbr)]




def mix_list(list_to_mix:list):
    L = list(list_to_mix)
    for i,e in enumerate(L):
        j = m.floor(random()*(i+1))
        L[i] , L[j] = L[j] , L[i]

    return L


def mix_list_v2(list_to_mix:list):
    ans = []
    fin = False
    i = 0
    while not fin:
        j = m.floor(random()*(len(list_to_mix)))
        if  list_to_mix[j] != None:
            ans.append(list_to_mix[j])
            list_to_mix[j] = None
            i += 1
        if i == len(list_to_mix):
            fin = True

    return ans

def testing_unit():
    l1 = ["Apple", "Asus", "Lenovo", "Dell", "MSI"]
    # print(gen_list_random_int(100, 12,43))
    # print(gen_list_random_int())
    print("LA LIST MIXEE")
    print(f"list de base = {l1} \n mix_list({l1}) = {mix_list(l1)} \n mix_list_v1({l1}) = {mix_list_v2(l1)}")
    lst_sorted=[i for i in range(10)]
    print(lst_sorted)
    print("Liste triée de départ",lst_sorted)
    mixed_list=mix_list(lst_sorted)
    print("Liste mélangée obtenue",mixed_list)
    print("Liste triée de départ après appel à mixList, elle doit être inchangée",lst_sorted)

def main():
    testing_unit()


if __name__ == "__main__":
    main()