import tkinter

def quartic(a, b, c, d, e, col):
    x = -5
    while x<=5:
        y = a*x*x*x*x + b*x*x*x + c*x*x + d*x + e
        x2 = x + 0.1
        y2 = a*x2*x2*x2*x2 + b*x2*x2*x2 + c*x2*x2 + d*x2 + e
        cx = x*20 + ox
        cy = oy - y*20
        cx2 = x2*20 + ox
        cy2 = oy - y2*20
        cvs.create_line(cx, cy, cx2, cy2, fill=col)
        x += 0.1

root = tkinter.Tk()
root.title("四次曲線")
cvs = tkinter.Canvas(width=600, height=600, bg="white")
cvs.pack()

ox = 300
oy = 300
cvs.create_text(ox+20, oy+15, text="(0,0)")

cvs.create_line(ox, 0, ox, 600, fill="gray") # Y軸
for y in range(0, 600, 20): # Y軸の目盛り
    cvs.create_line(ox-2, y, ox+3, y, fill="silver")
cvs.create_line(0, oy, 600, oy, fill="gray") # X軸
for x in range(0, 600, 20): # Y軸の目盛り
    cvs.create_line(x, oy-2, x, oy+3, fill="silver")

quartic(1, -16/3, 6, 0, 3, "red")
quartic(-1, 0, 2, 0, -1, "blue")
root.mainloop()