f = open("test.txt", 'r', encoding="utf-8")
r = f.read()
f.close()
s = r.split(",")
n = len(s)
data = [0]*n
for i in range(n):
    if s[i] != "":
        data[i] = int(s[i])
print(data)