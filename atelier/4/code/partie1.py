import random
import math as m

def gen_list_random_int(int_nbr=10, int_binf=0, int_bsub=10)->list:
    return [m.floor((random.random()*(int_bsub-int_binf+1))+int_binf) for e in range(int_nbr)]




def mix_list(list_to_mix:list):
    L = list(list_to_mix)
    for i,e in enumerate(L):
        j = m.floor(random.random()*(i+1))
        L[i] , L[j] = L[j] , L[i]

    return L


def mix_list_v2(list_to_mix:list):
    ans = []
    fin = False
    i = 0
    while not fin:
        j = m.floor(random.random()*(len(list_to_mix)))
        if  list_to_mix[j] != None:
            ans.append(list_to_mix[j])
            list_to_mix[j] = None
            i += 1
        if i == len(list_to_mix):
            fin = True

    return ans


def choose_element_list(list_in_which_to_choose:list):
    return  list_in_which_to_choose[random.randint(0, len(list_in_which_to_choose) - 1)] if len(list_in_which_to_choose)!= 0  else None

def extract_elements_list(list_in_which_to_choose:list, int_nbr_of_element_to_extract:int):
    ans = []

    if int_nbr_of_element_to_extract > len(list_in_which_to_choose):
        ans = list_in_which_to_choose
    else:
        L = list(list_in_which_to_choose)
        for i in range(int_nbr_of_element_to_extract):
            ran_index = random.randint(0, len(L) - 1)
            elem = L.pop(ran_index)
            ans.append(elem)
    return ans

def extract_elements_list_v1(lst:list, k:int):
    n = len(lst)
    result = [None] * k
    pool = list(lst)
    for i in range(k):
        j = random.randint(0,n - i - 1)
        result[i] = pool[j]
        pool[j] = pool[n - i - 1]
    return result

def extract_elements_list_v2(lst:list, k:int):
    n = len(lst)
    result = [None] * k
    selected = set()
    for i in range(k):
        j = random.randint(0,n-1)
        while j in selected:
            j = random.randint(0,n-1)
        selected.add(j)
        result[i] = lst[j]
    return result










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

    print("Exercice 3")
    # Test de votre code
    print('Liste triée de départ',lst_sorted)
    e1 = choose_element_list(lst_sorted)
    print('A la première exécution',e1,'a été sélectionné')
    e2 = choose_element_list(lst_sorted)
    print('A la deuxième exécution',e2,'a été sélectionné')
    assert e1 != e2
    print("Exercice 4")
    # Test de votre code
    print('Liste de départ',lst_sorted)
    sublist = extract_elements_list_v2(lst_sorted,5)
    print('La sous liste extraite est',sublist)
    print('Liste de départ après appel de la fonction est',lst_sorted)





def main():
    testing_unit()


if __name__ == "__main__":
    main()