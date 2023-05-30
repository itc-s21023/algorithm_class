data = [
    ["佐藤", "000-0000-0000"],
    ["鈴木", "111-1111-1111"],
    ["高橋", "222-2222-2222"],
    ["田中", "333-3333-3333"]
]
n = len(data)
s = input("検索する相手の苗字は? ")
data.append(s)
i = 0
while i < n and data[i][0] != s:
    i += 1
if i == n:
    print("その名は登録されていません")
    choice = input("登録しますか？ (はい/いいえ): ")
    if choice == "はい":
        number = input("電話番号を入力してください: ")
        data.append([s, number])
        print(s + "さんの電話番号 " + number + " を登録しました")
    else:
        data.append([s, ""])
        print(s + "さんを登録しました")
else:
    print(data[i][0] + "さんの番号は " + data[i][1] + "です")