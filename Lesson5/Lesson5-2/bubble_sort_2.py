data = [9, 4, 7, 2, 3, 8, 6, 1, 5, 0]
n = len(data)
print(data, "元のデータ")

for i in range(0, n-1):
    for j in range(0, n-1-i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print(data, "ソート後のデータ")