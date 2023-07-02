x = 3

match x:
    case 0:
        print("case 0")
    case 1:
        print("case 1")
    case 2:
        print("case 2")
    case _ if x == 3:
        print("case 3 default")
    case _:
        print("case default")