import tkinter
import math

def tree(x, y, leng, a):
    if leng <= 4:
        return
    nx = x + leng*math.cos(math.radians(a))
    ny = y + leng*math.sin(math.radians(a))
    cvs.create_line(x, y, nx, ny, fill="white")
    tree(nx, ny, leng*0.75, a-30)
    tree(nx, ny, leng*0.75, a+30)

root = tkinter.Tk()
root.title("樹木曲線")
cvs = tkinter.Canvas(width=800, height=600, bg="black")
cvs.pack()
tree(400, 600, 160, -90)
root.mainloop()