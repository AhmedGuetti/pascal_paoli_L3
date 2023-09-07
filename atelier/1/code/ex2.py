def est_bissextile (year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 and year % 400 != 0 


def func_test() :
    for year in range(1000, 2024):
        ans = est_bissextile(year)
        print(f"[{year}]", end =' -----------> ')
        if ans:
            print("True")
        else:
            print("False") 

func_test()

