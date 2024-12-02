#!/usr/bin/python3
"""
Module pour calculer le périmètre d'une île dans une grille.
"""


def island_perimeter(grid):
    """
    Retourne le périmètre de l'île décrite dans la grille.

    Args:
        grid (liste de listes d'int): La grille représentant l'île.

    Returns:
        int: Le périmètre de l'île.
    """
    if not grid or not grid[0]:
        return 0

    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Commence avec 4 côtés pour chaque cellule de terre
                perimeter += 4

                # Vérifie si la cellule au-dessus est de la terre
                if i > 0 and grid[i - 1][j] == 1:
                    # Soustrait 2 pour le côté partagé avec la cellule du dessus
                    perimeter -= 2
                # Vérifie si la cellule à gauche est de la terre
                if j > 0 and grid[i][j - 1] == 1:
                    # Soustrait 2 pour le côté partagé avec la cellule de gauche
                    perimeter -= 2

    return perimeter
