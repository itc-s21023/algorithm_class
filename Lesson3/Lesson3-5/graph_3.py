data = [
    [0, 1, 1, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 1, 1, 0]
]

node = ["那覇", "糸満", "沖縄", "宜野湾", "名護"]
arrow = ["", "-->", "<--", "<->"]

for y in range(5):
    for x in range(5):
        if data[y][x] == 1:
            print(node[y] + arrow[1] + node[x])
        elif data[y][x] == 0 and data[x][y] == 1:
            print(node[y] + arrow[3] + node[x])
