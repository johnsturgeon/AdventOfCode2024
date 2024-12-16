import os
import sys
from typing import List

os.environ["DAY"] = "01"


def get_distance(input_list: List) -> int:
    left_list, right_list = get_split_list(input_list)
    left_list.sort()
    right_list.sort()
    total_distance: int = 0
    for index, _ in enumerate(left_list):
        total_distance += abs(left_list[index] - right_list[index])
    return total_distance

def get_similarities(input_list: List) -> int:
    total_similarity_score: int = 0
    left_list, right_list = get_split_list(input_list)
    for item in left_list:
        total_similarity_score += item * right_list.count(item)
    return total_similarity_score

def get_split_list(input_list: List):
    left_list: List[int] = []
    right_list: List[int] = []
    for line in input_list:
        l,r = line.split()
        left_list.append(int(l))
        right_list.append(int(r))
    return left_list, right_list


    
