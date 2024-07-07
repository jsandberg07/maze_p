from graphics import Cell, Point

class Maze:
    def __init__(
            self, 
            x1, 
            y1, 
            num_rows, 
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__create_cells()

    def __create_cells(self):
        self.__cells = []
        # if you ever forget how hard you're working
        # remember you got this on your first try
        # you plan, you work, you try really hard
        # and it's paying off
        # even if you don't believe, there are still results
        for x in range(0, self.__num_cols):
            new_col = []
            x1 = self.__x1 + ((x + 0) * self.__cell_size_x)
            x2 = self.__x1 + ((x + 1) * self.__cell_size_x)
            for y in range(0, self.__num_rows):
                y1 = self.__y1 + ((y + 0) * self.__cell_size_y)
                y2 = self.__y1 + ((y + 1) * self.__cell_size_y)
                p1 = Point(x1, y1)
                p2 = Point(x2, y2)
                new_col.append(Cell(p1, p2, self.__win))
            self.__cells.append(new_col)
        
        for x in range(0, self.__num_cols):
            for y in range(0, self.__num_cols):
                self.__cells[x][y].draw()


