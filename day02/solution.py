"""
Advent of Code 2025 - Day 2
"""

import time
import re

def parse_input(input_text):
    lines = input_text.split(',')
    return lines


def part1(data):

    invalid_numbers = []
    for i in data:
        my_range = list(range(int(i.split('-')[0]), int(i.split('-')[1])+1))
        for j in my_range:
            j = str(j).lstrip('0')
            mid = len(j) // 2
            if len(j) % 2 == 0:
                left_half = j[:mid]
                right_half = j[mid:]
                is_invalid = (left_half == right_half)
            else:
                is_invalid = False 
            
            if(is_invalid):
                invalid_numbers.append(j)
    sum = 0
    for i in invalid_numbers:
        sum += int(i)

    return sum


def part2(data):
    invalid_numbers = []
    for i in data:
        my_range = list(range(int(i.split('-')[0]), int(i.split('-')[1])+1))
        for j in my_range:
            j = str(j).lstrip('0')
            is_invalid = bool(re.fullmatch(r"(.+)\1+", str(j)))
            if is_invalid:
                invalid_numbers.append(j)
    sum = 0
    for i in invalid_numbers:
        sum += int(i)

    return sum


if __name__ == "__main__":
    with open("day02/input.txt") as f:
        input_text = f.read()
    
    data = parse_input(input_text)
    
    # Part 1
    start = time.perf_counter()
    result1 = part1(data)
    end = time.perf_counter()
    print(f"Part 1: {result1} ({(end - start) * 1000:.2f}ms)")
    
    # Part 2
    start = time.perf_counter()
    result2 = part2(data)
    end = time.perf_counter()
    print(f"Part 2: {result2} ({(end - start) * 1000:.2f}ms)")
