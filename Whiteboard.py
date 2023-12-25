import tkinter as tk

class WhiteBoard:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Whiteboard")

        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack(side=tk.RIGHT, padx=10, pady=10)  # Place canvas on the right side with padding

        self.setup_buttons()

        self.old_x = None
        self.old_y = None
        self.drawing_color = "black"  # Default drawing color

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

    def setup_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(side=tk.LEFT, padx=10)  # Place button frame on the left side with padding

        clear_button = tk.Button(button_frame, text="Clear", command=self.clear_board)
        clear_button.pack(pady=5)

        red_button = tk.Button(button_frame, text="Red", command=self.set_red_color)
        red_button.pack(pady=5)

        black_button = tk.Button(button_frame, text="Black", command=self.set_black_color)
        black_button.pack(pady=5)

        black_button = tk.Button(button_frame, text="Green", command=self.set_green_color)
        black_button.pack(pady=5)

        black_button = tk.Button(button_frame, text="Black", command=self.set_black_color)
        black_button.pack(pady=5)


    def paint(self, event):
        x, y = event.x, event.y
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, x, y, width=2, fill=self.drawing_color)
        self.old_x = x
        self.old_y = y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def clear_board(self):
        self.canvas.delete("all")

    def set_red_color(self):
        self.drawing_color = "red"

    def set_green_color(self):
        self.drawing_color = "green"
    def set_black_color(self):
        self.drawing_color = "black"

def main():
    root = tk.Tk()
    whiteboard = WhiteBoard(root)
    root.mainloop()

if __name__ == "__main__":
    main()
