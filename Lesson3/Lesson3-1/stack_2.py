MAX = 5
stack = [0] * MAX
sp = 0

def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp = sp + 1
        print("データ", d, "を追加")
    else:
        print("これ以上データを入れられません")

def pop():
    global sp
    if sp > 0:
        sp = sp - 1
        return stack[sp]
    else:
        print("データが存在しない")
        return None

push(1)
push(2)

popped_item = pop()
if popped_item is not None:
    print("データ", popped_item, "を取り出した")
else:
    print("スタックは空")

push(3)
push(4)
push(5)

print(stack)

