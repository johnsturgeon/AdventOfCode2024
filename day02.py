import os
from typing import List, Optional

os.environ["DAY"] = "02"

def levels_increase(levels: List[int]) -> bool:
    def get_break_index(levels) -> int:
        previous_level: int = 0
        for index, level in enumerate(levels):
            # always skip the first element
            level: int = int(level)
            if index == 0:
                previous_level = level
                continue
            if previous_level >= level:
                break_index = index
                return break_index
            previous_level = level
        return -1

    break_index: int = get_break_index(levels)
    if break_index == -1:
        return levels_safe(levels)
    return break_index
    

def levels_decrease(levels: List[int]) -> bool:
    def get_break_index(levels) -> int:
        previous_level: int = 0
        for index, level in enumerate(levels):
            # always skip the first element
            level: int = int(level)
            if index == 0:
                previous_level = level
                continue
            if previous_level <= level:
                break_index = index
                return break_index
            previous_level = level
        return -1

    break_index: int = get_break_index(levels)
    if break_index == -1:
        return levels_safe(levels)
    return break_index

def levels_safe(levels: List[int]) -> bool:
    previous_level: Optional[int] = None
    for index, level in enumerate(levels):
        level: int = int(level)
        if previous_level:
            diff = abs(level - previous_level)
            if diff > 3 or diff < 1 :
                return index
        previous_level = level
    return -1

def safe_report_count(input_list: List, use_mulligan: bool = False) -> int:
    count: int = 0
    for levels in input_list:
        levels = levels.split()
        increase_ok: int = levels_increase(levels) == -1 
        decrease_ok: int = levels_decrease(levels) == -1
        if increase_ok or decrease_ok:
            count += 1
    return count


def safe_report_with_mulligan(input_list: List) -> int:
    count: int = 0
    for levels in input_list:
        levels = levels.split()
        increase_ok: int = levels_increase(levels) == -1 
        decrease_ok: int = levels_decrease(levels) == -1
        if increase_ok or decrease_ok:
            count += 1
            continue
        for index, _ in enumerate(levels):
            new_list: List = levels.copy()
            new_list.pop(index)
            increase_ok: int = levels_increase(new_list) == -1 
            decrease_ok: int = levels_decrease(new_list) == -1
            if increase_ok or decrease_ok:
                count += 1
                break

    return count
