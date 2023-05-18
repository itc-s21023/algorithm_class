for i in range(1, 10):
    k = ""
    for j in range(1, 10):
        k = k + "{}x{}={:2d}  ".format(j, i, i*j)
    print(k)