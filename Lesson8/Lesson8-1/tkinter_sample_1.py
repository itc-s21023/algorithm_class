import tkinter
root = tkinter.Tk()
root.title("ウィンドウのタイトル")
cvs = tkinter.Canvas(width=600, height=400, bg="white")
cvs.pack()
cvs.create_line(0, 0, 500, 300)
root.mainloop()