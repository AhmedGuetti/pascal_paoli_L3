def est_bissextile (year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0 )or year % 400 == 0 


def func_test_1() :
    for year in range(1800, 2024):
        ans = est_bissextile(year)
        print(f"[{year}]", end =' -----------> ')
        if ans:
            print("True")
        else:
            print("False") 



def func_test_2() :
        ans = est_bissextile(400)
        print(f"[400]", end =' -----------> ')
        if ans:
            print("True")
        else:
            print("False") 




func_test_1()
func_test_2()


