LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1,    2,    10],
    [3,    4,    20],
    [5,    None, 30],
    [None, None, 40],
    [6,    7,    50],
    [None, None, 60],
    [None, None, 70],
    [None, None, 80]
]
MAX = len(node)

print("指定の番号のノードを調べます")
print("何も入力せずにEnterを押すと終了します")

while True:
    lf = input("number=")
    if lf == "":
        break
    n = int(lf)
    if 0 <= n and n < MAX:
        print("node{}の値は{}".format(n, node[n][DATA]))
    else:
        print("0から{}の範囲で入力してください".format(MAX-1))
