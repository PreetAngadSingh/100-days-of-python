x = int(input("Enter the value of x:"))

# x is the variabel to match
match x:
    # if x is 0
    case 0:
        print("x is zero")
    # if x is 4
    case 0:
        print("case is 4")
    # in python we can add if statement to the defaut cases as well
    case _ if x==90:
        print("x = 90, the case is default")
    # default case
    case _:
        print("default case running")