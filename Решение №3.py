for A in range(1, 300):
    flag = False
    for x in range(0, 300):
        for y in range(0, 300):
            f1 = ((x%35 != 0) and (x%A == 0)) <= (x%21 == 0)
            f2 = (x > 20) or (y > 30) or ((y + 2 * x) < A)
            if (f1 and f2) == False:
                flag = True
                break
        if flag == True:
            break
    if flag == False:
        print(A, end = '; ')
