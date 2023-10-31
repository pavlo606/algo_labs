from tkinter import Tk, Canvas, Button, Frame, Label
from flood_fill import read_file, flood_fill

MAX_SIZE = 600

colors = {
    "W": "#f0f0f0",
    "X": "#222222",
    "R": "#ee2023",
    "G": "#22ee22",
    "B": "#2222ee",
    "Y": "#eeee22",
    "Gr": "#aaaaaa",
    "P": "#ee22ee"
}

class Window:
    def __init__(self, matrix, width, height):
        self.width = width
        self.height = height
        self.matrix = matrix

        self.canvas_width = MAX_SIZE if width >= height else int(MAX_SIZE * width / height)
        self.canvas_height = MAX_SIZE if width <= height else int(MAX_SIZE * height / width)

        self.rect_width = self.canvas_width / self.width
        self.rect_height = self.canvas_height / self.height

        self.root = Tk()
        self.root.title("Flood Fill")
        self.canvas = Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack(side="left")
        self.canvas.bind('<Button-1>', self.canvas_click)

        self.selected_color = "Gr"
        self.color_selector = Frame(self.root)
        self.color_selector.pack(side="right")
        Button(self.color_selector, text="Set default matrix", command=self.clear).pack(pady=5)
        self.btn_frame = Frame(self.color_selector)
        self.btn_frame.pack()
        for color in colors.keys():
            Button(self.btn_frame, text="", width=5, height=2, background=colors[color], \
                    command=lambda c=color: self.color_btn_click(c)).pack(side="right")
        Label(self.color_selector, text="Selected color:").pack()
        self.current_color_frame = Frame(self.color_selector, background=colors[self.selected_color], width=42, heigh=42)
        self.current_color_frame.pack()
    
    def drawRects(self):
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.canvas.create_rectangle(x * self.rect_width, y * self.rect_height, \
                                        (x * self.rect_width) + self.rect_width, (y * self.rect_height) + self.rect_height, \
                                        fill=colors[self.matrix[y][x]])
                
    def canvas_click(self, event):
        print('Clicked canvas: ', event.x, event.y, event.widget)
        x = int(event.y / self.rect_width)
        y = int(event.x / self.rect_height)
        self.matrix = flood_fill(self.matrix, self.width, self.height, x, y, self.selected_color)
        self.drawRects()

    def color_btn_click(self, color):
        self.selected_color = color
        self.current_color_frame.configure(background=colors[color])

    def clear(self):
        matrix, *_ = read_file()
        self.matrix = matrix
        self.drawRects()

if __name__ == "__main__":
    matrix, width, height, *_ = read_file()
    
    window = Window(matrix, width, height)
    window.drawRects()

    window.root.mainloop()