score = [70, 98, 92, 88, 64]
total = 0
for i in range(5):
    total = total + score[i]
average = total / 5
print("合計点", total)
print("平均点", average)