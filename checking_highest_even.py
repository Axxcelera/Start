def highest_even(list):
    list.sort()
    for i in range(len(list)):
        a = list.pop()
        if a%2==0:
            print(f"highest even is {a}")
            break

highest_even([2,15,41,25,43,25])
