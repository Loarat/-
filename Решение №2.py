for A in range(1, 500):
    flag = False
    for x in range(1, 500):
        if ( (((x%A != 0) and (x%54 == 0)) <= (x%36 != 0)) and ((x<=6) <= (x**2<=A)) ) == False:
            flag = True
            break
    if flag == False:
        print(A)
