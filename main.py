from window import Window
from graphics import Line, Point, Cell

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

def main():
    win = Window(SCREEN_WIDTH, SCREEN_HEIGHT)
    # black_box(win)
    test_cells(win)
    win.wait_for_close()

def black_box(win):
# draw some lines

    # top left
    p0 = Point(20, 20)
    # top right
    p1 = Point(SCREEN_WIDTH - 20, 20)
    # bottom left
    p2 = Point(20, SCREEN_HEIGHT - 20)
    # bottom right
    p3 = Point(SCREEN_WIDTH - 20, SCREEN_HEIGHT - 20)
    
    the_array = [p0, p1, p2, p3]
    drawn = 0

    for outer in range(0, len(the_array)):
        for inner in range(outer, len(the_array)):
            line = Line(the_array[outer], the_array[inner])
            if outer != inner:
                win.draw_line(line, "black")
                drawn += 1

    
    print(f"// lines drawn: {drawn}")

def test_cells(win):
    x_coords = []
    y_coords = []

    
    x = (SCREEN_WIDTH / 10)
    y = (SCREEN_HEIGHT / 10)
    for x_mult in range(0, 10):
        x_coords.append(x * x_mult)
    x_coords.pop(0)
    x_coords.pop(-1)
    print(x_coords)


    for y_mult in range(0, 10):
        y_coords.append(y * y_mult)
    y_coords.pop(0)
    y_coords.pop(-1)
    print(y_coords)

    for x in range(0, len(x_coords) - 1):
        for y in range(0, len(y_coords) - 1):
            p1 = Point(x_coords[x], y_coords[y])
            p2 = Point(x_coords[x+1], y_coords[y+1])
            cell = Cell(p1, p2, win)
            if x % 2 == 0:
                cell.has_top_wall = False
                cell.has_bottom_wall = False
            if y % 2 == 0:
                cell.has_left_wall = False
                cell.has_right_wall = False
            cell.draw()
            



    # p1 = Point(20, 20)
    # p2 = Point(30, 30)
    # cell1 = Cell(p1, p2, win)
    # cell1.draw()
    

main()