max_A = -1
for A in range(0, 100):
    flag = False
    for x in range(0, 100):
        if ( (x&A != 0) <= ((x&40 != 0) <= (x&26 != 0)) ) == False:
            flag = True
            break
    if flag == False:
        max_A = max(max_A, A)
print(max_A)
