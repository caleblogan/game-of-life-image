from time import sleep
from copy import deepcopy


class GameOfLife:
    def __init__(self, graph):
        self.graph = graph

    def run(self, gen_sleep_seconds=.1, max_gens=100):
        """
        Starts running the game.
        Runs up untill max gens or forever if max_gens is -1
        :param max_gens: how many generations to run, -1 = forever
        :param gen_sleep_seconds: how long to sleep in between generations
        :return:
        """
        cur_gen = 0
        while max_gens == -1 or cur_gen < max_gens:
            self.advance_generation()
            sleep(gen_sleep_seconds)
            cur_gen += 1
        return max_gens

    def advance_generation(self):
        """
        Advances one generation of the game.
        Handles the logic killing/reviving cells.
        Each cell is determined alive or dead simultaneously (use a copy of the graph).
        :return:
        """
        graph_copy = deepcopy(self.graph._data)
        for row in range(len(graph_copy)):
            for col in range(len(graph_copy[0])):
                n_alive = self.n_neighbors_alive(row, col)
                cell = graph_copy[row][col]
                if self.should_live(cell.is_alive, n_alive):
                    cell.revive()
                else:
                    cell.kill()
        self.graph._data = graph_copy

    def n_neighbors_alive(self, row, col):
        """Returns the number of neighbors alive"""
        return len([cell for cell in self.graph.neighbors(row, col) if cell.is_alive])

    def should_live(self, is_alive, n_alive):
        """
        The logic to determine if a cell should continue to live, continue to be dead, die, revive
        :param is_alive: True if the cell is currently alive
        :param n_alive: the number of neighbors alive
        :return: True if cell should live other wise False
        """
        if is_alive:
            return n_alive == 2 or n_alive == 3
        else:
            return n_alive == 3


class GameGraph:
    """
    Used to represent the graph for the cells in the game of life.
    """
    def __init__(self, input_arr):
        """Creates an length X width graph composed of Cells from an array of 1s and 0s"""
        self._data = self._generate_graph(input_arr)

    def neighbors(self, row, col):
        """Gets a list of neighbor cells at a row and col"""
        neighbors_list = []
        # top-left
        if self.is_valid_index(row-1, col-1):
            neighbors_list.append(self._data[row-1][col-1])
        # top
        if self.is_valid_index(row-1, col):
            neighbors_list.append(self._data[row-1][col])
        # top-right
        if self.is_valid_index(row-1, col+1):
            neighbors_list.append(self._data[row-1][col+1])
        # right
        if self.is_valid_index(row, col+1):
            neighbors_list.append(self._data[row][col+1])
        # bottom-right
        if self.is_valid_index(row+1, col+1):
            neighbors_list.append(self._data[row+1][col+1])
        # bottom
        if self.is_valid_index(row+1, col):
            neighbors_list.append(self._data[row+1][col])
        # bottom-left
        if self.is_valid_index(row+1, col-1):
            neighbors_list.append(self._data[row+1][col-1])
        # left
        if self.is_valid_index(row, col-1):
            neighbors_list.append(self._data[row][col-1])

        return neighbors_list

    def is_valid_index(self, row, col):
        if row < 0 or row >= len(self._data):
            return False
        elif col < 0 or col >= len(self._data[0]):
            return False
        return True

    def _generate_graph(self, input_arr):
        """
        :param input_arr: an array of nXm 1s and 0s representing whether a cell should be alive.
        :return:
        """
        data = []
        for row in range(len(input_arr)):
            data.append([])
            for col in range(len(input_arr[0])):
                data[row].append(Cell(input_arr[row][col]))
        return data


class Cell:
    """
    Represents each alive or dead entity in the graph.
    """
    def __init__(self, is_alive):
        self.is_alive = is_alive

    def kill(self):
        self.is_alive = False

    def revive(self):
        self.is_alive = True
