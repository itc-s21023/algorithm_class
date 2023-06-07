LEFT = 0
RIGHT = 1
DATA = 2

node = [
    [1, 2, "38.5℃の発熱があるか"],
    [3, 4, "胸がひいひい"],
    [5, 6, "元気はあるか"],
    [None, None, "速攻で病院"],
    [None, None, "解熱剤で病院"],
    [None, None, "様子見"],
    [None, None, "氷枕で病院"],
]

MAX = len(node)

print("38.5℃以上の発熱がある？")
print("何も入力せずにEnterを押すと終了")

while True:
    s = input("回答を入力してください (Yes/No): ")
    if s == "":
        break

    n = 0
    if s.lower() == "no":
        n = 2
        print("元気がある？")
    elif s.lower() == "yes":
        n = 1
        print("胸がひいひい？")
    else:
        print("YesまたはNoで回答してください")
        continue

    s = input("回答を入力してください (Yes/No): ")
    if s == "":
        break

    if n == 1:
        if s.lower() == "no":
            print("解熱剤で病院")
            break  # 処理を終了
        elif s.lower() == "yes":
            print("速攻で病院")
            break  # 処理を終了
        else:
            print("YesまたはNoで回答してください")

    elif n == 2:
        if s.lower() == "no":
            print("氷枕で病院")
            break  # 処理を終了
        elif s.lower() == "yes":
            print("様子を見る")
            break  # 処理を終了
        else:
            print("YesまたはNoで回答してください")
    else:
        print("不正な入力です")
