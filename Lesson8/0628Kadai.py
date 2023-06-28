import tkinter

maze = [
    [99]*15,
    [99, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 99],
    [99, 0,99,99, 0,99,99, 0,99,99,99,99,99,99, 99],
    [99,99,99, 0, 0, 0,99, 0,99, 0, 0, 0, 0,99, 99],
    [99, 0, 0, 0,99, 0, 0, 0,99, 0,99,99, 0,99, 99],
    [99, 0,99, 0, 0, 0,99, 0,99, 0,99,99, 0,99, 99],
    [99,99,99,99,99,99,99,99,99,99,99,99,99,99, 99]
]
FNT = ("Times New Roman", 16)
start_x = 13
start_y = 1
goal_x = 1
goal_y = 5
goal = False
steps = 0

def walk():
    global goal, steps
    steps += 1
    for y in range(1, 6):
        for x in range(1, 14):
            if maze[y][x] == steps:
                if maze[y-1][x] == 0:
                    maze[y-1][x] = steps+1
                if maze[y+1][x] == 0:
                    maze[y+1][x] = steps+1
                if maze[y][x-1] == 0:
                    maze[y][x-1] = steps+1
                if maze[y][x+1] == 0:
                    maze[y][x+1] = steps+1
    if maze[goal_y][goal_x] != 0:
        goal = True
        shortest_way()

def shortest_way():
    s = maze[goal_y][goal_x]
    x = goal_x
    y = goal_y
    while s > 0:
        print("({},{})".format(x, y))
        maze[y][x] += 100
        s -= 1
        if maze[y-1][x] == s:
            y -= 1
        elif maze[y+1][x] == s:
            y += 1
        elif maze[y][x-1] == s:
            x -= 1
        elif maze[y][x+1] == s:
            x += 1

def draw_maze():
    cvs.delete("all")
    for y in range(7):
        for x in range(15):
            col = "white"
            if maze[y][x] == 99:
                col = "gray"
            if maze[y][x] > 100:
                col = "yellow"
            cx = 40 * x
            cy = 40 * y
            cvs.create_rectangle(cx, cy, cx+38, cy+38, fill=col, width=0)
            cvs.create_text(cx+20, cy+20, text=str(maze[y][x]%100), font=FNT)
            if x==start_x and y==start_y:
                cvs.create_text(cx+20, cy+8, text="start", font=FNT, fill="red")
            if x==goal_x and y==goal_y:
                cvs.create_text(cx+20, cy+8, text="goal", font=FNT, fill="blue")

def main():
    if goal == False:
        walk()
    draw_maze()
    root.after(1000, main)

root = tkinter.Tk()
root.title("迷路を解く")
cvs = tkinter.Canvas(width=600, height=280)
cvs.pack()
maze[start_y][start_x] = 1
main()
root.mainloop()
