import os, re
import math

from typing import List, Optional

os.environ["DAY"] = "03"

def get_mul(input_list: List[int]) -> int:
    line: str
    result = 0
    for line in input_list:
        muls = re.findall('mul\(\d{1,3},\d{1,3}\)', line)
        for mul in muls:
            digits = re.findall('\d+', mul)
            int_digits: List[int] = list(map(int, digits))
            result += math.prod(int_digits)
    return result

def get_mul2(input_list: List[int]) -> int:
    result = 0
    all_lines = ""
    line: str
    for line in input_list:
        all_lines += line.rstrip()
    do_strings = all_lines.split("do()")
    for string in do_strings:
        do_instruction = string
        dont_index = string.find("don't()")
        if dont_index != -1:
            do_instruction = string[:dont_index]
        result += get_mul([do_instruction])

    return result