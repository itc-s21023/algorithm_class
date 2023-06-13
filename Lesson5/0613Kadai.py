data = [9, 4, 7, 2, 3, 8, 6, 1, 5, 0]
n = len(data)
print(data, "元のデータ")

for i in range(0, n-1):
    for j in range(n-1, i, -1):
        if data[j-1] > data[j]:
            data[j], data[j-1] = data[j-1], data[j]

sorted_data = data.copy()
for i in range(len(sorted_data)):
    if i != len(sorted_data) - 1:
        print(sorted_data[i], end=', ')
    else:
        print('\033[31m' + str(sorted_data[i]) + '\033[0m', end=' ')
print("ソート後のデータ")
