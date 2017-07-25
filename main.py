import tkinter as tk
import argparse

from game_of_life import GameOfLife, GameGraph
from game_of_life.gui import Application
from game_of_life.image_processing import convert_to_seed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Play Conways Game of Life with images.')
    parser.add_argument('img_path', nargs='?',
                        default='./images/giants_morse_behind_enemy_lines.jpg',
                        help='The path of the image to seed the game with.')
    args = parser.parse_args()
    print(f'Using image path: {args.img_path}')

    seed_data = convert_to_seed(args.img_path)
    game = GameOfLife(GameGraph(seed_data))

    root = tk.Tk()
    app = Application(game, cell_size=10, generation_sleep=300, master=root)
    app.mainloop()
