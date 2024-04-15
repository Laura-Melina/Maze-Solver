from tkinter import Tk, BOTH, Canvas


from window import Window,Point,Line
from cell import Cell
from maze import Maze
def main():
    win = Window(820,620)

    maze = Maze(10,10,16,12,50,50,win,5)
    
    win.wait_for_close()

main()