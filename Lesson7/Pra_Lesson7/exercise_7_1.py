text = "I'm learning Python. It's interesting!"
pattern = "python"
tn = len(text)
pn = len(pattern)
flg = False
p = 0
sim = -1

while p <= tn-pn:
    c = 0
    for i in range(pn):
        if text[p+i] == pattern[i]:
            c += 1
    if c == pn:
        flg = True
        break
    if c >= pn*0.75:
        sim = p
    p += 1

print(text)
if flg == True:
    print(str(p+1)+"文字目に"+pattern+"があります")
else:
    print(pattern+"は見つかりませんでした")
    if sim >= 0:
        print("が", sim+1, "文字目に類似する文字列が見つかりました")