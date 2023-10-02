def closezero(mylist:list)->float:
    """_summary_

    Args:
        mylist (list): _description_
    Returns:
        float: _description_
    """
    ans = abs(mylist[0])
    for e in mylist:
        if abs(e) < ans:
            ans = e
    return ans



def closezero_v2(l):
    # l.sort()
    ans = l[0]
    for e in l:
        if e < 0:
            if abs(e) > ans:
                ans = e
        else:
            if abs(e) < ans:
                ans = e
    return ans





def testing_unit():
    test_list= [
        [7,-1,13,8,4,-1.2,1,2,3,-2],
        [7,-10,13,8,4,-7.2,12,-3.7,3.5,-1.7,2]
    ]

    for test in test_list:
        print(closezero_v2(test))


def main():
    testing_unit()

if __name__ == "__main__":
    main()




        