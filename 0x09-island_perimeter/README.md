# 0x09. Island Perimeter

## Description

Ce projet consiste à calculer le périmètre d'une île dans une grille. L'île est représentée par des `1` (terre) et l'eau est représentée par des `0`. Chaque cellule de la grille est carrée et a une longueur de côté de 1. Les cellules sont connectées horizontalement ou verticalement (pas en diagonale). La grille est entièrement entourée d'eau, et il n'y a qu'une seule île (ou aucune). L'île ne contient pas de "lacs" (eau à l'intérieur qui n'est pas connectée à l'eau entourant l'île).

## Objectifs d'apprentissage

À la fin de ce projet, vous devriez être capable de :

- Comprendre comment naviguer et manipuler des matrices (listes 2D) en Python.
- Appliquer une logique conditionnelle pour déterminer les conditions de calcul du périmètre.
- Développer un algorithme efficace pour résoudre des problèmes géométriques dans un contexte de grille.

## Exigences du projet

- **Langage de programmation :** Python 3.4.3
- **Style de code :** PEP 8 (version 1.7)
- **Interdictions :**
  - Vous ne pouvez pas importer de modules externes.
  - Vous devez utiliser des boucles et des conditions natives de Python.
- **Fichiers :**
  - Tous vos fichiers doivent se terminer par une nouvelle ligne.
  - La première ligne de tous vos fichiers doit être `#!/usr/bin/python3`.
  - Votre code doit être documenté (modules, fonctions, méthodes, classes).

## Fichiers

- `0-island_perimeter.py` : Contient la fonction `island_perimeter(grid)` qui calcule le périmètre de l'île.
- `0-main.py` : Script principal pour tester la fonction avec un exemple de grille.

## Utilisation

Pour tester la fonction, vous pouvez exécuter le script principal :

```bash
$ ./0-main.py
```

**Exemple de sortie :**

```
12
```

## Fonctionnement de la fonction `island_perimeter`

La fonction `island_perimeter(grid)` prend en entrée une grille (liste de listes d'entiers) et retourne un entier représentant le périmètre de l'île.

**Algorithme :**

1. **Initialisation :**
   - Vérifier si la grille est vide ou si la première ligne est vide.
   - Initialiser une variable `perimeter` à 0.
   - Déterminer le nombre de lignes (`rows`) et de colonnes (`cols`) de la grille.

2. **Parcours de la grille :**
   - Parcourir chaque cellule de la grille à l'aide de boucles imbriquées.

3. **Identification des cellules de terre :**
   - Si une cellule contient un `1` (terre) :
     - Ajouter 4 au périmètre (chaque cellule de terre a 4 côtés potentiels).

4. **Vérification des côtés partagés :**
   - **Cellule au-dessus :**
     - Si la cellule n'est pas dans la première ligne (`i > 0`) et que la cellule au-dessus est de la terre (`grid[i - 1][j] == 1`) :
       - Soustraire 2 du périmètre (côté partagé).
   - **Cellule à gauche :**
     - Si la cellule n'est pas dans la première colonne (`j > 0`) et que la cellule à gauche est de la terre (`grid[i][j - 1] == 1`) :
       - Soustraire 2 du périmètre (côté partagé).

5. **Résultat :**
   - Après avoir parcouru toutes les cellules, retourner la valeur du périmètre.

## Exemple de grille

Voici un exemple de grille et le calcul de son périmètre :

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
```

**Visualisation de la grille :**

- Les `1` représentent l'île.
- Les `0` représentent l'eau.

Le périmètre calculé pour cette grille est `12`.


## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
