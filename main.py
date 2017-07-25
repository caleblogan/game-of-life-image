import tkinter as tk

from game_of_life import GameOfLife, GameGraph
from game_of_life.gui import Application


if __name__ == '__main__':
    data = [
        [1, 0, 0, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    game = GameOfLife(GameGraph(data))

    root = tk.Tk()
    app = Application(game, cell_size=10, master=root)
    app.mainloop()
