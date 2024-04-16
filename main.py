from tkinter import Tk, BOTH, Canvas


from window import Window,Point,Line
from cell import Cell
from maze import Maze
def main():
    win = Window(820,620)

    maze = Maze(10,10,32,24,25,25,win)
    maze.solve()
    win.wait_for_close()

main()