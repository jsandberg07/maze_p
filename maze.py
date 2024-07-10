from graphics import Cell, Point
import time
import random

class Maze:
    def __init__(
            self, 
            x1, 
            y1, 
            num_rows, 
            num_cols, 
            cell_size_x, 
            cell_size_y, 
            win=None,
            seed=None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__seed = seed
        if seed:
            random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

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

        self.__draw_maze()

    def __draw_maze(self):
        for x in range(0, self.__num_cols):
            for y in range(0, self.__num_rows):
                    self.__cells[x][y].draw()

    def __draw_cell(self, i, j):
        if self.__win == None:
            return
        self.__cells[i][j].draw()
    

    def __animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(.05)

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_left_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_right_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            # hold i and j values needed to visit
            # check cells that are adjacent, keep track that have not been visited
            to_visit = self.__get_adjacent_to_visit(i, j)
            # if 0 directions, draw current cell and return to break loop
            if len(to_visit) == 0:
                return
            # otherwise, prick random directon (shuffle array and pick the first one)
            random.shuffle(to_visit)
            target = to_visit.pop(0)
            # knock down walls between current and chosen cell
            i, j = self.__remove_walls_target(i, j, target)
            # move to chosen cell by calling resursively
            print(f"// going {target}")
            print(f"// using coords {i}, {j}")
            self.__break_walls_r(i, j)


    # change this to be strings, then you can say "go up", not deal with sets
    def __get_adjacent_to_visit(self, i, j):
        # would be [i - 1 j], [i + 1 j], [i j - 1], [i j + 1], and not visited
        to_visit = []
        # left
        if i - 1 >= 0:
            if self.__cells[i - 1][j].visited == False:
                to_visit.append("left")
                # to_visit.append(set(i - 1, j))
        # right
        if i + 1 < self.__num_cols:
            if self.__cells[i + 1][j].visited == False:
                to_visit.append("right")
                # to_visit.append(set(i + 1, j))
        # up
        if j - 1 >= 0:
            if self.__cells[i][j - 1].visited == False:
                to_visit.append("up")
                # to_visit.append(set(i, j - 1))
        # down
        if j + 1 < self.__num_rows:
            if self.__cells[i][j + 1].visited == False:
                to_visit.append("down")
                # to_visit.append(set(i, j + 1))

        return to_visit


    def __remove_walls_target(self, i, j, target):
        if target == "up":
            self.__cells[i][j - 1].has_bottom_wall = False
            self.__draw_cell(i, j-1)
            self.__cells[i][j].has_top_wall = False
            self.__draw_cell(i, j)
            return i, j-1

        elif target == "down":
            self.__cells[i][j + 1].has_top_wall = False
            self.__draw_cell(i, j+1)
            self.__cells[i][j].has_bottom_wall = False
            self.__draw_cell(i, j)
            return i, j+1

        elif target == "left":
            self.__cells[i - 1][j].has_right_wall = False
            self.__draw_cell(i-1, j)
            self.__cells[i][j].has_left_wall = False
            self.__draw_cell(i, j)
            return i-1, j

        elif target == "right":
            self.__cells[i + 1][j].has_left_wall = False
            self.__draw_cell(i+1, j)
            self.__cells[i][j].has_right_wall = False
            self.__draw_cell(i, j)
            return i+1, j

        else:
            raise ValueError("Not proper direction handled by __remove_walls_target")
        
        


