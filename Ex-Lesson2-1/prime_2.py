p = [True] * 81
p[0] = False
p[1] = False
n = 2

def hyou():
    count = 0
    s = ""
    for i in range(81):
        if p[i] == True:
            s += "{:2d}, ".format(i)
            count += 1
        else:
            s += "/, "
        if i % 9 == 8:
            s += "\n"
    print(s)
    print("素数は" + str(count) + "です")

def furui():
    global n
    for i in range(n+n, 81, n):
        p[i] = False
    print(n, "の倍数をふるい落としました")
    hyou()
    while n < 81 :
        n = n + 1
        if p[n] == True:
            break

hyou()
while n < 9:
    input("Enterキーを押せ")
    furui()



