import os, re
import math

from typing import List, Optional

os.environ["DAY"] = "04"

class Point(object):
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Point):
            return self.X == other.X and self.Y == other.Y
        return False

def build_grid(input_list: List) -> List[List[str]]:
    puzzle: List[List[str]] = []
    for row_number, row in enumerate(input_list):
        row_list: List = []
        for cell in row:
            row_list.append(cell)
        puzzle.append(row_list)
    return puzzle

def find_paths(in_grid, start_row, start_col) -> int:
    count = 0
    if in_grid[start_row][start_col] != "X":
        return 0
    directions: List[Point] = [
        Point(0, -1),
        Point(0, 1),
        Point(1, -1),
        Point(1, 0),
        Point(1, 1),
        Point(-1, -1),
        Point(-1, 0),
        Point(-1, 1),
    ]
    for point in directions:
        search_point1: Point = Point(start_row + point.X*1, start_col + point.Y*1)
        search_point2: Point = Point(start_row + point.X*2, start_col + point.Y*2)
        search_point3: Point = Point(start_row + point.X*3, start_col + point.Y*3)
        if (search_point1.X >= 0 and search_point1.Y >=0 and
            search_point2.X >= 0 and search_point2.Y >=0 and
            search_point3.X >= 0 and search_point3.Y >=0):
            try:
                if (in_grid[search_point1.X][search_point1.Y] == "M" and
                in_grid[search_point2.X][search_point2.Y] == "A" and
                in_grid[search_point3.X][search_point3.Y] == "S"):
                    count += 1
            except IndexError:
                pass
    return count

def find_mas(in_grid, start_row, start_col) -> int:
    count = 0
    # search dir 1 for MAS or SAM
    try:
        word = in_grid[start_row+1][start_col+1]
        word += in_grid[start_row][start_col]
        word += in_grid[start_row-1][start_col-1]
        if word == "MAS" or word == "SAM":
            word2 = in_grid[start_row+1][start_col-1]
            word2 += in_grid[start_row][start_col]
            word2 += in_grid[start_row-1][start_col+1]
            if word2 == "MAS" or word2 == "SAM":
                count += 1
    except IndexError:
        pass

    return count


def get_xmases(input_list: List) -> int:
    grid: List[List[str]] = build_grid(input_list)
    counter = 0
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            counter += find_paths(grid, x, y)
    return counter

def get_mases(input_list: List) -> int:
    grid: List[List[str]] = build_grid(input_list)
    counter = 0
    for x, row in enumerate(grid):
        for y, char in enumerate(row):
            if char == "A":
                counter += find_mas(grid, x, y)
    return counter
