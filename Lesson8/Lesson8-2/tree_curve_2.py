import tkinter
import math

def color(val): # RGB値の色を作る関数
    if val > 255:
        val = 255
    col = "#{:02x}{:02x}{:02x}".format(0, val, 255-val)
    return col

def tree(x, y, leng, ang, c):
    if leng < 3: # これより短くなったら再帰しない
        return

    # 枝の先の座標
    nx = x + int(leng*math.cos(math.radians(ang)))
    ny = y + int(leng*math.sin(math.radians(ang)))

    w = int(leng/8)+1 # 線の幅を決める
    cvs.create_line(x, y, nx, ny, fill=color(c), width=w) # 線を引く
    cvs.update()

    # 再帰呼び出し
    tree(nx, ny, int(leng*0.75), ang-30, c+24) # 左へ
    tree(nx, ny, int(leng*0.75), ang+30, c+24) # 右へ

root = tkinter.Tk()
root.title("樹木曲線")
cvs = tkinter.Canvas(width=800, height=600, bg="black")
cvs.pack()
tree(400, 600, 160, -90, 0)
root.mainloop()