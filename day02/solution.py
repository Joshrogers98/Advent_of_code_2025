"""
Advent of Code 2025 - Day 2
"""

import time


def parse_input(input_text):
    """Parse the input"""
    lines = input_text.strip().split('\n')
    return lines


def part1(data):
    """Solve part 1"""
    pass


def part2(data):
    """Solve part 2"""
    pass


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
