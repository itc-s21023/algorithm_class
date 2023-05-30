data = [57, 48, 46, 52, 45, 59, 61, 60, 49, 71]
n = len(data)
key = 60
flg = False
for i in range(n):
    if data[i] == key:
        print("data[{}]が{}です".format(i, key))
        flg = True
        break
if flg == False:
    print(str(key)+"は存在しません")