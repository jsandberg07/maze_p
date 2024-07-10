class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, 
                           fill=fill_color, width=2)
        

class Cell:
    def __init__(self, p1, p2, win=None):
        self.__x1 = p1.x
        self.__y1 = p1.y
        self.__x2 = p2.x
        self.__y2 = p2.y

        self.__win = win

        self.has_top_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True

        self.visited = False

    # draw a line for each wall
    def draw(self):
        
        p1 = Point(self.__x1, self.__y1)
        p2 = Point(self.__x2, self.__y1)
        line = Line(p1, p2)
        if self.has_top_wall:
            self.__win.draw_line(line, "black")
        else:
            self.__win.draw_line(line, "white")

        
        p1 = Point(self.__x2, self.__y1)
        p2 = Point(self.__x2, self.__y2)
        line = Line(p1, p2)
        if self.has_right_wall:
            self.__win.draw_line(line, "black")
        else:
            self.__win.draw_line(line, "white")

        
        p1 = Point(self.__x1, self.__y1)
        p2 = Point(self.__x1, self.__y2)
        line = Line(p1, p2)
        if self.has_left_wall:
            self.__win.draw_line(line, "black")
        else:
            self.__win.draw_line(line, "white")

        p1 = Point(self.__x1, self.__y2)
        p2 = Point(self.__x2, self.__y2)
        line = Line(p1, p2)
        if self.has_bottom_wall:
            self.__win.draw_line(line, "black")
        else:
            self.__win.draw_line(line, "white")

    def draw_move(self, to_cell, undo=False):
        # between two cells
        # so find the midpoint of each by averaging the cells as a point
        # then draw the line between them duh
        p1 = self.get_midpoint()
        p2 = to_cell.get_midpoint()
        line = Line(p1, p2)
        draw_color = "red"
        if undo:
            draw_color = "gray"
        self.__win.draw_line(line, draw_color)
        
    def get_midpoint(self):
        x = ((self.__x1 + self.__x2) / 2)
        y = ((self.__y1 + self.__y2) / 2)
        return Point(x, y)



