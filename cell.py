from window import Point,Line,Window


class Cell():
    def __init__(self,window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

      
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall == True:
            line_left = Line(Point(self._x1,self._y1),Point(self._x1,self._y2))
            self._win.draw_line(line_left)
        if self.has_right_wall == True:
            line_right = Line(Point(self._x2,self._y1),Point(self._x2,self._y2))
            self._win.draw_line(line_right)
        if self.has_top_wall == True:
            line_top = Line(Point(self._x1,self._y1),Point(self._x2,self._y1))
            self._win.draw_line(line_top)
        if self.has_bottom_wall == True:
            line_bottom = Line(Point(self._x1,self._y2),Point(self._x2,self._y2))
            self._win.draw_line(line_bottom)

   
    def draw_move(self, to_cell, undo = False):
        if self._win is None:
            return

        mid_x = (self._x1 + self._x2)/2
        mid_y = (self._y1 + self._y2)/2
        to_mid_x = (to_cell._x1 + to_cell._x2)/2
        to_mid_y = (to_cell._y1 + to_cell._y2)/2
        
        fill_color = "red"
        if undo == True:
            fill_color = "gray"

        line = Line(Point(mid_x,mid_y),Point(to_mid_x,to_mid_y))
        self._win.draw_line(line,fill_color)    