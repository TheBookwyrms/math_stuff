def N_getter(max):
    beg1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    beg2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]   
    for number in beg1:
        basenum = beg1[number-1]
        for i in beg2:
            basenum2 = int(str(basenum) + str(beg2[i-1]))
            str2 = (f'{(basenum2**2):04d}')
            str2 = str(str2)
            num3 = str2[1]
            num4 = str2[2]
            num5 = int(str(num3) + str(num4))
            
            if num5 == max:
                a = [True, basenum2]
                return a
    a = [False, None]
    return(a)


def squareChecker(max):
    a = [False, None]
    while a[0] == False:
        max = max
        a = N_getter(max)
        if a[0] == False:
            max = max - 1
        else:
            return(a)


def doubleChecker(max):
    a = squareChecker(max)
    b = (f'{(a[1]**2):04d}')
    c = str(b)
    d = c[1]
    e = c[2]
    f = int(str(d) + str(e))
    if max == f:
        return(a)
    else:
        return(False)


if __name__ == "__main__":
    max = int(input("What number would you like to check?\n"))
    print(doubleChecker(max))