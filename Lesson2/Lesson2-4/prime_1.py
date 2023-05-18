for i in range(2, 101):
    h = i//2
    f = True
    for j in range(2, h+1):
        if i%j == 0:
            f = False
            break
    if f == True:
        print(i, end=",")