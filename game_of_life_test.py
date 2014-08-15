#!/usr/bin/env python
# encoding: utf-8

from sets import Set

import unittest

from game_of_life import GameOfLife


class TestGameOfLife(unittest.TestCase):
    def setUp(self):
        self.game_of_life = GameOfLife()
        self._cells_alive = None

    def tearDown(self):
        self._cells_alive = None
        self.game_of_life = None

    def test_any_live_cell_with_fewer_than_two_live_neighbours_dies_example_1(self):
        self.game_of_life.set_alive_cells(((0, 0),))
        self._assert_cells_are_dead_in_next_generation((0, 0))

    def test_any_live_cell_with_fewer_than_two_live_neighbours_dies_example_2(self):
        self.game_of_life.set_alive_cells(((0, 0), (0, 1)))
        self._assert_cells_are_dead_in_next_generation(((0, 0), (0, 1)))

    def test_any_live_cell_with_fewer_than_two_live_neighbours_dies_example_3(self):
        self.game_of_life.set_alive_cells(((0, 0),
                                           (1, 0)))
        self._assert_cells_are_dead_in_next_generation(((0, 0),
                                                        (1, 0)))

    def test_any_live_cell_with_more_than_three_live_neighbours_dies_example_1(self):
        self.game_of_life.set_alive_cells((        (0, 1),
                                           (1, 0), (1, 1), (1, 2),
                                                   (2, 1)))
        self._assert_cells_are_dead_in_next_generation((1, 1))

    def test_any_live_cell_with_more_than_three_live_neighbours_dies_example_2(self):
        self.game_of_life.set_alive_cells(((0, 0), (0, 1),
                                           (1, 0), (1, 1), (1, 2),
                                                   (2, 1)))
        self._assert_cells_are_dead_in_next_generation((1, 1))

    def test_any_live_cell_with_more_than_three_live_neighbours_dies_example_3(self):
        self.game_of_life.set_alive_cells(((0, 0), (0, 1), (0, 2),
                                           (1, 0), (1, 1), (1, 2),
                                                   (2, 1)))
        self._assert_cells_are_dead_in_next_generation((1, 1))

    def test_any_live_cell_with_more_than_three_live_neighbours_dies_example_4(self):
        self.game_of_life.set_alive_cells(((0, 0), (0, 1), (0, 2),
                                           (1, 0), (1, 1), (1, 2),
                                           (2, 0), (2, 1)))
        self._assert_cells_are_dead_in_next_generation((1, 1))

    def test_any_live_cell_with_more_than_three_live_neighbours_dies_example_5(self):
        self.game_of_life.set_alive_cells(((0, 0), (0, 1), (0, 2),
                                           (1, 0), (1, 1), (1, 2),
                                           (2, 0), (2, 1), (2, 2)))
        self._assert_cells_are_dead_in_next_generation((1, 1))

    def test_any_live_cell_with_two_or_three_live_neighbours_lives_on_example_1(self):
        self.game_of_life.set_alive_cells((        (0, 1),
                                           (1, 0),         (1, 2),
                                                   (2, 1)))
        self._assert_cells_are_alive_in_next_generation((        (0, 1),
                                                         (1, 0),         (1, 2),
                                                                 (2, 1)))

    def test_any_live_cell_with_two_or_three_live_neighbours_lives_on_example_2(self):
        self.game_of_life.set_alive_cells((        (0, 1),
                                           (1, 0), (1, 1), (1, 2),
                                                   (2, 1)))
        self._assert_cells_are_alive_in_next_generation((        (0, 1),
                                                         (1, 0),         (1, 2),
                                                                 (2, 1)))

    def test_any_dead_cell_with_exactly_three_live_neighbours_becomes_alive(self):
        self.game_of_life.set_alive_cells((        (0, 1),
                                           (1, 0), (1, 1), (1, 2),
                                                   (2, 1)))
        self._assert_cells_are_alive_in_next_generation(((0, 0),       (0, 2),
                                                         (2, 0),       (2, 2)))

    def test_suggested_example(self):
        self.game_of_life.set_alive_cells((        (1, 4),
                                           (2, 3), (2, 4)))
        self._assert_exactly_these_cells_are_alive_in_next_generation(
            ((1, 3), (1, 4),
             (2, 3), (2, 4)))

    def test_oscillation(self):
        initially_alive_cells = ((0, 0), (0, 1), (0, 2))
        self.game_of_life.set_alive_cells(initially_alive_cells)
        self._assert_exactly_these_cells_are_alive_in_next_generation(
            ((-1, 1),
             ( 0, 1),
             ( 1, 1)))
        self._assert_exactly_these_cells_are_alive_in_next_generation(initially_alive_cells)

    def test_glider(self):
        self.game_of_life.set_alive_cells(
            (        (0, 1),
                             (1, 2),
             (2, 0), (2, 1), (2, 2)))

        self._assert_exactly_these_cells_are_alive_in_next_generation(
            (
             (1, 0),         (1, 2),
                     (2, 1), (2, 2),
                     (3, 1)))

        self._assert_exactly_these_cells_are_alive_in_next_generation(
            (
                             (1, 2),
             (2, 0),         (2, 2),
                     (3, 1), (3, 2)))

        self._assert_exactly_these_cells_are_alive_in_next_generation(
            (
                     (1, 1),
                             (2, 2), (2, 3),
                     (3, 1), (3, 2)))

        self._assert_exactly_these_cells_are_alive_in_next_generation(
            (
                             (1, 2),
                                     (2, 3),
                     (3, 1), (3, 2), (3, 3)))

    def _assert_cells_are_dead_in_next_generation(self, cells):
        self._cells_alive = self.game_of_life.get_next_generation()
        self.assertEqual(Set(), Set(cells) & self._cells_alive)

    def _assert_cells_are_alive_in_next_generation(self, cells):
        self._cells_alive = self.game_of_life.get_next_generation()
        self.assertTrue(Set(cells) <= self._cells_alive)

    def _assert_exactly_these_cells_are_alive_in_next_generation(self, cells):
        self._cells_alive = self.game_of_life.get_next_generation()
        self.assertEqual(Set(cells), self._cells_alive)

def run_unit_tests():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestGameOfLife)
    unittest.TextTestRunner(verbosity=2).run(test_suite)

run_unit_tests()
