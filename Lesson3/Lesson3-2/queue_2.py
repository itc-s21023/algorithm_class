MAX_SIZE = 6
queue = [0] * MAX_SIZE
head = 0
tail = 0

def get_queue_contents():
    i = head
    contents = []
    while i % MAX_SIZE != tail: # キューの要素を順番に取得
        contents.append(queue[i])
        i = (i + 1) % MAX_SIZE
    return contents

def enqueue(data):
    global tail
    next_tail = (tail + 1) % MAX_SIZE # 次の末尾インデックスを計算

    if next_tail == head:
        print('待ちが満杯')
    else:
        queue[tail] = data
        tail = next_tail
        count = len(get_queue_contents()) # 現在の待ち時間を計算
        print(f'待ち時間: {count * 15}分')

def dequeue():
    global head
    if head == tail:
        print('取り出すデータが存在しません')
        return None
    else:
        data = queue[head]
        queue[head] = 0
        head = (head + 1) % MAX_SIZE
        print(f'{data}が待ちから出ました')
        return data

for i in range(3):
    enqueue(i)

for i in range(2):
    dequeue()

enqueue(i)
