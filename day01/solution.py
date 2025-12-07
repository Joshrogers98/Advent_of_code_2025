"""
Advent of Code 2025 - Day 1
"""

import time
import re

def parse_input(input_text):
    lines = input_text.strip().split('\n')
    return lines


def part1(data):
    current_position = 50
    times_hit_zero = 0
    for i in data :
        if(i.startswith("L")):
            integer_value = int(re.findall(r'\d+', i)[0])
            current_position -= integer_value
        else:
            integer_value = int(re.findall(r'\d+', i)[0])
            current_position += integer_value

        current_position = current_position % 100
        if(current_position == 0):
            times_hit_zero += 1
    return times_hit_zero


def part2(data):
    current_position = 50
    times_hit_zero = 0

    #print( "The dial starts pointing at " + str(current_position))

    for i in data :

        output_string = "The dial is rotated [" + i + "] to point at "

        if(i.startswith("L")):
            zeros_this_loop = 0
            integer_value = int(re.findall(r'\d+', i)[0])
            while integer_value > 0:
                current_position -= 1
                integer_value -= 1
                if(current_position == 0):
                    zeros_this_loop += 1
                    times_hit_zero += 1
                current_position = current_position % 100

        if(i.startswith("R")):
            zeros_this_loop = 0
            integer_value = int(re.findall(r'\d+', i)[0])
            while integer_value > 0:
                current_position += 1
                integer_value -= 1
                if(current_position == 100):
                    zeros_this_loop += 1
                    times_hit_zero += 1
                current_position = current_position % 100   

        if(zeros_this_loop == 0 or current_position == 0):
            output_string += "[" + str(current_position) + "]." 
        else:
            output_string += "[" + str(current_position) + "]" + "; during this rotation, the dial hit 0 a total of [" + str(zeros_this_loop) + "] times."


        
        #print(output_string)

    return times_hit_zero

if __name__ == "__main__":
    with open("day01/input.txt") as f:
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
