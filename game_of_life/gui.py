import tkinter as tk


class Application(tk.Frame):
    def __init__(self, game, cell_size=10, generation_sleep=500, master=None):
        super().__init__(master)
        self.pack()
        self.game = game
        self.cell_size = cell_size
        self.generation_sleep = generation_sleep
        self.create_widgets()
        self.after(generation_sleep, self.advance_generation)

    def create_widgets(self):
        self.canvas = tk.Canvas(self)
        self.canvas.pack()
        self.draw_grid()

    def draw_grid(self):
        game_data = self.game.graph._data
        rows = len(game_data)
        cols = len(game_data[0])
        cell_size = self.cell_size
        start_x = 0
        start_y = 0

        for row in range(rows):
            for col in range(cols):
                color = 'green' if game_data[row][col].is_alive else 'white'
                self.draw_cell(start_x+col*cell_size, start_y+row*cell_size, cell_size, cell_size, color)

    def draw_cell(self, x, y, width, height, fill):
        self.canvas.create_rectangle(x, y, x+width, y+height, fill=fill)

    def advance_generation(self):
        self.game.advance_generation()
        self.draw_grid()
        self.after(self.generation_sleep, self.advance_generation)
