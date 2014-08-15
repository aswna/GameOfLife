#!/usr/bin/env python
# encoding: utf-8

from sets import Set


class GameOfLife(object):
    def __init__(self, alive_cells=None):
        self._alive_cells = Set(alive_cells)

    def set_alive_cells(self, alive_cells):
        self._alive_cells = Set(alive_cells)

    def get_next_generation(self):
        self._alive_cells = self._get_surviving_cells() | self._get_newborn_cells()
        return self._alive_cells

    def _get_surviving_cells(self):
        surviving_cells = Set()
        for cell in self._alive_cells:
            number_of_alive_neighbors = self._get_number_of_alive_neighbors(cell)
            if 2 <= number_of_alive_neighbors < 4:
                surviving_cells.add(cell)
        return surviving_cells

    def _get_newborn_cells(self):
        newborn_cells = Set()
        for cell in self._get_all_dead_neighbors():
            number_of_alive_neighbors = self._get_number_of_alive_neighbors(cell)
            if number_of_alive_neighbors == 3:
                newborn_cells.add(cell)
        return newborn_cells

    def _get_number_of_alive_neighbors(self, cell):
        return len(self._alive_cells & self._get_neighbors(cell))

    def _get_all_dead_neighbors(self):
        dead_neighbors = Set()
        for cell in self._alive_cells:
            dead_neighbors |= self._get_dead_neighbors(cell)
        return dead_neighbors

    def _get_dead_neighbors(self, cell):
        return self._get_neighbors(cell) - self._alive_cells

    def _get_neighbors(self, cell):
        (row, col) = cell
        neighbors = Set(((row - 1, col - 1),
                         (row - 1, col    ),
                         (row - 1, col + 1),
                         (row    , col - 1),
                         (row    , col + 1),
                         (row + 1, col - 1),
                         (row + 1, col    ),
                         (row + 1, col + 1)))
        return neighbors
