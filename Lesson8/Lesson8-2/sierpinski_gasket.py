import tkinter

def tri(x, y, s):
    h = s*1.732/2
    cvs.create_line(x-s/2, y-h/2, x+s/2, y-h/2)
    cvs.create_line(x-s/2, y-h/2, x, y+h/2)
    cvs.create_line(x+s/2, y-h/2, x, y+h/2)
    if s > 10:
        tri(x, y-h/2-h/4, s/2)
        tri(x-s/2, y+h/4, s/2)
        tri(x+s/2, y+h/4, s/2)

root = tkinter.Tk()
root.title("シェルピンスキーのギャスケット")
cvs = tkinter.Canvas(width=800, height=600, bg="white")
cvs.pack()
tx = 400
ty = 300
si = 600
he = si*1.732/2
cvs.create_line(tx, ty-he/2, tx-si/2, ty+he/2, tx+si/2, ty+he/2, tx, ty-he/2)
tri(tx, ty+he/4, si/2)
root.mainloop()