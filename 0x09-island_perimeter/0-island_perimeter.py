#!/usr/bin/python3
"""
Create a function def island_perimeter(grid):
that returns the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes”
(water inside that isn’t connected to the water surrounding the island).
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    Args:
        grid: 2d list of integers containing 0(water) or 1(land)
    Return:
        the perimeter of the island
    """

    p = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (grid[i][j] == 1):
                if (i <= 0 or grid[i - 1][j] == 0):
                    p += 1
                if (i >= len(grid) - 1 or grid[i + 1][j] == 0):
                    p += 1
                if (j <= 0 or grid[i][j - 1] == 0):
                    p += 1
                if (j >= len(grid[i]) - 1 or grid[i][j + 1] == 0):
                    p += 1
    return p
