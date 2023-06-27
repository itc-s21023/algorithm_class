import tkinter

maze = [
    [99,99,99,99,99,99,99,99,99],
    [99, 0, 0, 0, 0, 0, 0, 0,99],
    [99, 0,99,99, 0,99,99, 0,99],
    [99,99,99, 0, 0, 0,99, 0,99],
    [99, 0, 0, 0,99, 0, 0, 0,99],
    [99, 0,99, 0, 0, 0,99, 0,99],
    [99,99,99,99,99,99,99,99,99]
]
FNT = ("Times New Roman", 16)
start_x = 7
start_y = 1
goal_x = 1
goal_y = 5
goal = False
steps = 0

def walk():
    global goal, steps
    steps += 1
    for y in range(1, 6):
        for x in range(1, 8):
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
        for x in range(9):
            col = "white"
            if maze[y][x] == 99:
                col = "gray"
            if maze[y][x] > 100:
                col = "cyan"
            cx = 60 * x
            cy = 60 * y
            cvs.create_rectangle(cx, cy, cx+58, cy+58, fill=col, width=0)
            cvs.create_text(cx+30, cy+30, text=str(maze[y][x]%100), font=FNT)
            if x==start_x and y==start_y:
                cvs.create_text(cx+30, cy+10, text="start", font=FNT, fill="red")
            if x==goal_x and y==goal_y:
                cvs.create_text(cx+30, cy+10, text="goal", font=FNT, fill="blue")

def main():
    if goal == False:
        walk()
    draw_maze()
    root.after(1000, main)

root = tkinter.Tk()
root.title("迷路を解く")
cvs = tkinter.Canvas(width=540, height=420)
cvs.pack()
maze[start_y][start_x] = 1
main()
root.mainloop()