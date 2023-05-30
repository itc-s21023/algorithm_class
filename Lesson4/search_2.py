data = [57, 48, 46, 52, 45, 59, 61, 60, 49, 71]
n = len(data)
key = 60
i = 0
while i < n and data[i] != key:
    i += 1
if i == n:
    print(str(key)+"は存在しません")
else:
    print("data[{}]が{}です".format(i, key))