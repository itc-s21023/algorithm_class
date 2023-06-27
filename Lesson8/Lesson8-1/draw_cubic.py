import tkinter

def cubic(a, b, c, d, col):
    x = -1
    while x<=4:
        y = a*x*x*x + b*x*x + c*x + d
        x2 = x + 0.1
        y2 = a*x2*x2*x2 + b*x2*x2 + c*x2 + d
        cx = x*30 + ox
        cy = oy - y*30
        cx2 = x2*30 + ox
        cy2 = oy - y2*30
        cvs.create_line(cx, cy, cx2, cy2, fill=col)
        x += 0.1

root = tkinter.Tk()
root.title("三次曲線")
cvs = tkinter.Canvas(width=600, height=600, bg="white")
cvs.pack()

ox = 300
oy = 300
cvs.create_text(ox+20, oy+15, text="(0,0)")

cvs.create_line(ox, 0, ox, 600, fill="gray") # Y軸
for y in range(0, 600, 30): # Y軸の目盛り
    cvs.create_line(ox-2, y, ox+3, y, fill="silver")
cvs.create_line(0, oy, 600, oy, fill="gray") # X軸
for x in range(0, 600, 30): # Y軸の目盛り
    cvs.create_line(x, oy-2, x, oy+3, fill="silver")

cubic(1, -5, 2, 8, "green")
root.mainloop()