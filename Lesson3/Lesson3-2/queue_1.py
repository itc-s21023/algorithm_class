MAX = 6
que = [0] * MAX
head = 0
tail = 0

def enqueue(d):
    global tail
    nt = (tail + 1) % MAX
    if nt == head:
        print("これ以上入れられません")
    else:
        que[tail] = d
        tail = nt
        print("データ", d, "を追加")
        wait_time = (tail - head) * 15
        print("待ち時間:", wait_time, "分")

def dequeue():
    global head
    if head == tail:
        print("取り出すデータがない")
        return None
    else:
        d = que[head]
        head = (head + 1) % MAX
        return d


enqueue(1)
enqueue(2)
enqueue(3)
dequeue()
dequeue()
enqueue(4)


