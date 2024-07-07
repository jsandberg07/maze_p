from tkinter import Tk, BOTH, Canvas
from graphics import Line

class Window:
    def __init__(self, width, height):
        # self.__width = width
        # self.__height = height
        self.__root = Tk()
        self.__root.title = "Hell yeah"
        self.__canvas = Canvas(self.__root, bg="#6481d2", height=height, width=width, )
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    # each time called, window will redraw itself
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("Window closed!")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)

