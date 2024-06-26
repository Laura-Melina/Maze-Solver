from window import Window
from cell import Cell
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_cols,
        num_rows, 
        cell_size_x,
        cell_size_y,
        win=None,
        seed = None
    ):
        self.x1 = x1 
        self.y1 = y1 
        self.num_cols = num_cols
        self.num_rows = num_rows
        
        
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._seed = seed
        if self._seed != None:
            random.seed(self._seed)
        self._cells = []
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        

    def _draw_cell(self,i,j):
        if self._win is None:
            return
        
        cell_x1 = self.x1 + (i * self.cell_size_x)
        cell_x2 = self.x1 + ((i+1) * self.cell_size_x)
        cell_y1 = self.y1 + (j * self.cell_size_y)
        cell_y2 = self.y1 + ((j + 1) * self.cell_size_y)
       
        self._cells[i][j].draw(cell_x1,cell_y1,cell_x2,cell_y2)
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.001)



    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    
    def _break_walls_r(self,i,j):
        
        self._cells[i][j].visited = True 
        
        
        while True:
            to_visit = []
            if 0 <= i+1 < self.num_cols:
                if self._cells[i+1][j].visited == False:
                    to_visit.append("Right")
            if 0 <= i-1 < self.num_cols:
                if self._cells[i-1][j].visited == False:
                    to_visit.append("Left")
                
            if 0 <= j+1 < self.num_rows:
                if self._cells[i][j+1].visited == False:
                    to_visit.append("Bottom")
            if 0 <= j-1 < self.num_rows:
                if self._cells[i][j-1].visited == False:
                    to_visit.append("Top")     

            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
                
            else:
                result = random.choice(to_visit)
                
                if result == "Bottom":
                    self._cells[i][j].has_bottom_wall = False
                    self._draw_cell(i,j)
                    self._cells[i][j+1].has_top_wall = False
                    self._draw_cell(i,j+1)
                    self._break_walls_r(i,j+1)
                
                if result == "Top":
                    self._cells[i][j].has_top_wall = False
                    self._draw_cell(i,j)
                    self._cells[i][j-1].has_bottom_wall = False
                    self._draw_cell(i,j-1)
                    self._break_walls_r(i,j-1)
                
                if result == "Right":
                    self._cells[i][j].has_right_wall = False
                    self._draw_cell(i,j)
                    self._cells[i+1][j].has_left_wall = False
                    self._draw_cell(i+1,j)
                    self._break_walls_r(i+1,j)

                if result == "Left":
                    self._cells[i][j].has_left_wall = False
                    self._draw_cell(i,j)
                    self._cells[i-1][j].has_right_wall = False
                    self._draw_cell(i-1,j)
                    self._break_walls_r(i-1,j)
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False 

    def solve(self):
        return self._solve_r(0,0)


    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited = True

        if self._cells[i][j] == self._cells[self.num_cols-1][self.num_rows-1]:
            return True

        if 0 <= j-1 < self.num_rows:
            if self._cells[i][j].has_top_wall == False and self._cells[i][j-1].visited == False:
                print("move up")
                self._cells[i][j].draw_move(self._cells[i][j-1],undo = False)
                if self._solve_r(i,j-1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j-1],undo = True)

        if 0 <= i-1 < self.num_cols:
            if self._cells[i][j].has_left_wall == False and self._cells[i-1][j].visited == False:
                print("move left")
                self._cells[i][j].draw_move(self._cells[i-1][j],undo = False)
                if self._solve_r(i-1,j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i-1][j],undo = True)

        if 0 <= j+1 < self.num_rows:
            if self._cells[i][j].has_bottom_wall == False and self._cells[i][j+1].visited == False:
                print("move down")
                self._cells[i][j].draw_move(self._cells[i][j+1],undo = False)
                if self._solve_r(i,j+1):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i][j+1],undo = True)
        if 0 <= i+1 < self.num_cols:
            if self._cells[i][j].has_right_wall == False and self._cells[i+1][j].visited == False:
                print("move right")
                self._cells[i][j].draw_move(self._cells[i+1][j],undo = False)
                if self._solve_r(i+1,j):
                    return True
                else:
                    self._cells[i][j].draw_move(self._cells[i+1][j],undo = True)

        
    
        return False