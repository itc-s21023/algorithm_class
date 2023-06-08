data = ["yuu", "seiga", "ryuuki", "yoshiya"]
print(data, "元のデータ")

for i in range(0, 3):
    m = i
    for j in range(i+1, 3):
        if data[j] < data[m]:
            m = j
    data[i], data[m] = data[m], data[i]

print(data, "ソート後のデータ")
