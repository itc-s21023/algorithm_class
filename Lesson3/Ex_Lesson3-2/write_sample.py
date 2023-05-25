f = open("test.txt", 'w', encoding="utf-8")
for i in range(1, 11):
    data = str(2**i)
    f.write(data+",")
f.close()