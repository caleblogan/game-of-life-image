import tkinter as tk
import PIL
from game_of_life import GameOfLife, GameGraph


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")


if __name__ == '__main__':
    # root = tk.Tk()
    # app = Application(master=root)
    # app.mainloop()
    data = [
        [1, 0, 0, 1],
        [0, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    game = GameOfLife(GameGraph(data))
    game.run(max_gens=2)