MAX = 7
data = [None] * MAX
pointer = [None] * MAX
head = 0

def add_list(d):
    n = -1
    for i in range(MAX):
        if data[i] == None:
            n = i
            break
    if n == -1:
        print("データ領域に空きがありません")
        return False
    for i in range(MAX):
        if data[i] != None and pointer[i] == None:
            pointer[i] = n
            break
    data[n] = d
    pointer[n] = None
    print("データ", d, "を追加しました")
    return True

def del_list(d):
    global head
    n = -1
    for i in range(MAX):
        if data[i] == d:
            n = i
            break
    if n == -1:
        print("そのデータは存在しません")
        return False
    if n != head:
        for i in range(MAX):
            if pointer[i] == n:
                pointer[i] = pointer[n]
    else:
        head = pointer[n]
        if head == None:
            head = 0
    data[n] = None
    pointer[n] = None
    print("データ", d, "を削除しました")
    return True

def put_list():
    p = head
    while True:
        print(data[p], end="→")
        if pointer[p] == None:
            print("EOF")
            break
        p = pointer[p]

add_list("赤")
add_list("橙")
add_list("黄")
add_list("緑")
add_list("青")
add_list("藍")
add_list("紫")

print("順番通り出力:")
put_list()

print("逆順で出力:")
stack = []
p = head
while True:
    stack.append(data[p])
    if pointer[p] == None:
        break
    p = pointer[p]

while stack:
    print(stack.pop(), end="→")
print("EOF")
