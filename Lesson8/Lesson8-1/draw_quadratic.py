import tkinter

def quadratic(a, b, c, col):
    x = -6
    while x<=10:
        y = a*x*x + b*x + c
        x2 = x+0.1
        y2 = a*x2*x2 + b*x2 + c
        cx = x*10 + ox
        cy = oy - y*10
        cx2 = x2*10 + ox
        cy2 = oy - y2*10
        cvs.create_line(cx, cy, cx2, cy2, fill=col)
        x += 0.1

root = tkinter.Tk()
root.title("二次曲線")
cvs = tkinter.Canvas(width=600, height=600, bg="white")
cvs.pack()

ox = 300
oy = 500
cvs.create_text(ox+20, oy+15, text="(0,0)")

cvs.create_line(ox, 0, ox, 600, fill="gray") # Y軸
for y in range(0, 600, 10): # Y軸の目盛り
    cvs.create_line(ox-2, y, ox+3, y, fill="silver")
cvs.create_line(0, oy, 600, oy, fill="gray") # X軸
for x in range(0, 600, 10): # Y軸の目盛り
    cvs.create_line(x, oy-2, x, oy+3, fill="silver")

quadratic(1, -4, -2, "blue")
root.mainloop()