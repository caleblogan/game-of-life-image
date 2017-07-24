import unittest
from copy import deepcopy

from game_of_life.game import GameOfLife
from game_of_life.game import GameGraph
from game_of_life.game import Cell


class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        self.input_data = [
            [1, 0, 0, 1],
            [0, 1, 1, 1],
            [0, 0, 0, 0]
        ]
        self.game = GameOfLife(GameGraph(self.input_data))

    def test_n_neighbors_alive(self):
        self.assertEqual(self.game.n_neighbors_alive(0, 0), 1)
        self.assertEqual(self.game.n_neighbors_alive(0, 3), 2)
        self.assertEqual(self.game.n_neighbors_alive(2, 2), 3)
        self.assertEqual(self.game.n_neighbors_alive(1, 2), 3)

    def test_should_live_alive_and_should_continue_living(self):
        self.assertTrue(self.game.should_live(True, 2))
        self.assertTrue(self.game.should_live(True, 3))

    def test_should_live_alive_and_should_die(self):
        self.assertFalse(self.game.should_live(True, 1))
        self.assertFalse(self.game.should_live(True, 10))

    def test_should_live_dead_and_should_stay_dead(self):
        self.assertFalse(self.game.should_live(False, 1))
        self.assertFalse(self.game.should_live(False, 5))

    def test_should_live_dead_and_should_reviev(self):
        self.assertTrue(self.game.should_live(False, 3))

    def test_advance_generation_no_alive(self):
        input_data = [
            [0, 0],
            [0, 0],
        ]
        game = GameOfLife(GameGraph(input_data))
        graph_before = deepcopy(game.graph._data)
        game.advance_generation()
        for row in range(len(game.graph._data)):
            for col in range(len(game.graph._data[0])):
                self.assertEqual(game.graph._data[row][col].is_alive, graph_before[row][col].is_alive)

    def test_advance_generation_all_alive(self):
        input_data = [
            [1, 1],
            [1, 1],
        ]
        game = GameOfLife(GameGraph(input_data))
        graph_before = deepcopy(game.graph._data)
        game.advance_generation()
        for row in range(len(game.graph._data)):
            for col in range(len(game.graph._data[0])):
                self.assertEqual(game.graph._data[row][col].is_alive, graph_before[row][col].is_alive)

    def test_advance_generation_simple_case(self):
        expected = [
            [False, True, False, True],
            [False, True, True, True],
            [False, False, True, False]
        ]
        self.game.advance_generation()
        graph_data = self.game.graph._data
        for row in range(len(graph_data)):
            for col in range(len(graph_data[0])):
                self.assertEqual(graph_data[row][col].is_alive, expected[row][col])

class TestGameGraph(unittest.TestCase):
    def setUp(self):
        self.input_data = [
            [1, 0, 0, 1],
            [0, 1, 1, 1],
            [0, 0, 0, 0]
        ]
        self.graph = GameGraph(self.input_data)

    def test__generate_graph_shape(self):
        g_data = self.graph._generate_graph(self.input_data)
        self.assertEqual(len(g_data), 3)
        self.assertEqual(len(g_data[0]), 4)

    def test__generate_graph_init_cells_zeros(self):
        input_data = [
            [0, 0],
            [0, 0]
        ]
        g_data = self.graph._generate_graph(input_data)
        for row in range(len(g_data)):
            for col in range(len(g_data[0])):
                self.assertFalse(g_data[row][col].is_alive)

    def test__generate_graph_init_cells_ones(self):
        input_data = [
            [1, 1],
            [1, 1]
        ]
        g_data = self.graph._generate_graph(input_data)
        for row in range(len(g_data)):
            for col in range(len(g_data[0])):
                self.assertTrue(g_data[row][col].is_alive)

    def test__generate_graph_simple(self):
        g_data = self.graph._generate_graph(self.input_data)
        for row in range(len(g_data)):
            for col in range(len(g_data[0])):
                self.assertEqual(g_data[row][col].is_alive, self.input_data[row][col])

    def test_neighbors_top_left(self):
        expected = [self.graph._data[0][1], self.graph._data[1][1], self.graph._data[1][0]]
        self.assertListEqual(self.graph.neighbors(0, 0), expected)

    def test_neighbors_top_right(self):
        expected = [self.graph._data[1][3], self.graph._data[1][2], self.graph._data[0][2]]
        self.assertListEqual(self.graph.neighbors(0, 3), expected)

    def test_neighbors_bottom_right(self):
        expected = [self.graph._data[1][2], self.graph._data[1][3], self.graph._data[2][2]]
        self.assertListEqual(self.graph.neighbors(2, 3), expected)

    def test_neighbors_bottom_left(self):
        expected = [self.graph._data[1][0], self.graph._data[1][1], self.graph._data[2][1]]
        self.assertListEqual(self.graph.neighbors(2, 0), expected)

    def test_neighbors_edge(self):
        expected = [
            self.graph._data[0][0], self.graph._data[0][1], self.graph._data[1][1],
            self.graph._data[2][1], self.graph._data[2][0]
        ]
        self.assertListEqual(self.graph.neighbors(1, 0), expected)

    def test_neighbors_completely_surrounded(self):
        expected = [
            self.graph._data[0][0], self.graph._data[0][1], self.graph._data[0][2],
            self.graph._data[1][2], self.graph._data[2][2], self.graph._data[2][1],
            self.graph._data[2][0], self.graph._data[1][0]
        ]
        self.assertListEqual(self.graph.neighbors(1, 1), expected)

    def test_is_valid_index_bad_input(self):
        self.assertFalse(self.graph.is_valid_index(-1, 0))
        self.assertFalse(self.graph.is_valid_index(0, -1))
        self.assertFalse(self.graph.is_valid_index(10, 0))

    def test_is_valid_index_good_input(self):
        self.assertTrue(self.graph.is_valid_index(0, 0))
        self.assertTrue(self.graph.is_valid_index(2, 2))
        self.assertTrue(self.graph.is_valid_index(1, 1))

class TestCell(unittest.TestCase):
    def test_init_is_alive_True(self):
        self.assertTrue(Cell(True).is_alive)

    def test_init_is_alive_False(self):
        self.assertFalse(Cell(False).is_alive)

    def test_kill(self):
        cell = Cell(True)
        cell.kill()
        self.assertFalse(cell.is_alive)

    def test_revive(self):
        cell = Cell(False)
        cell.revive()
        self.assertTrue(cell.is_alive)


if __name__ == '__main__':
    unittest.main()