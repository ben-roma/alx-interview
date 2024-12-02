#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): The grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Start with 4 sides for each land cell
                perimeter += 4

                # Check if the cell above is land
                if i > 0 and grid[i - 1][j] == 1:
                    # Subtract 2 for the shared side with the upper cell
                    perimeter -= 2
                # Check if the cell to the left is land
                if j > 0 and grid[i][j - 1] == 1:
                    # Subtract 2 for the shared side with the left cell
                    perimeter -= 2

    return perimeter
