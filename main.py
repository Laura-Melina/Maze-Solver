from tkinter import Tk, BOTH, Canvas


from window import Window,Point,Line
from cell import Cell

def main():
    win = Window(800,600)

 
    box = Cell(win)
    box.has_right_wall = False
    box.draw(50,50,100,100)

    box2 = Cell(win)
    box2.has_left_wall = False
    box2.draw(100,50,150,100)
    box.draw_move(box2,True)
    win.wait_for_close()

main()