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

s = input("number=")
if s != "":
    n = int(s)
    if 0 <= n < MAX:
        left_child = node[n][LEFT]
        data = node[n][DATA]

        print("node{}のLEFTの値は{}".format(n, left_child))
        print("node{}のDATAの値は{}".format(n, data))
    else:
        print("0から{}の範囲で入力してください".format(MAX-1))
