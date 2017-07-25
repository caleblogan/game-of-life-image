import tkinter as tk

from game_of_life import GameOfLife, GameGraph
from game_of_life.gui import Application
from game_of_life.image_processing import convert_to_seed


if __name__ == '__main__':
    data = [
        [1, 0, 0, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    seed_data = convert_to_seed('./images/giants_morse_behind_enemy_lines.jpg')
    game = GameOfLife(GameGraph(seed_data))

    root = tk.Tk()
    app = Application(game, cell_size=10, generation_sleep=300, master=root)
    app.mainloop()
