MAX = 6  #キューの最大指定
que = [0] * MAX
head = 0
tail = 0

def enqueue(d):
    global tail
    nt = (tail + 1) % MAX
    if nt == head:  #キューの空きがないなら
        print("これ以上入れられません")
    else:  #空きがあるなら
        que[tail] = d
        tail = nt
        print(d, "人待ちに入る")
        wait_time = (tail - head) * 15 ##待ち時間を表示する
        print("待ち時間:", wait_time, "分")

def dequeue():
    global head
    if head == tail:
        print("取り出すデータがない")
        return None
    else:
        d = que[head]
        head = (head + 1) % MAX
        print("待ちから", d, "人出る")
        wait_time = (tail - head) * 15
        print("待ち時間:", wait_time, "分")  #待ち時間を表示する
        return d


enqueue(1)
enqueue(2)
enqueue(3)
dequeue()
dequeue()
enqueue(4)
