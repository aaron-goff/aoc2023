from src.utils.helpers import read_file
import numpy as np

input = read_file("day2")

total = 0

def get_id_from_line(line):
    return int(line.split(":")[0].split(" ")[1])

def get_draws_as_list(line):
    draws = line.split(":")[1].replace(";", ",").split(",")
    return list(map(str.strip, draws))

def get_max_in_line(line):
    draws = get_draws_as_list(line)
    max = {
        'green': 0,
        'red': 0,
        'blue': 0
    }
    for draw in draws:
        number, color = draw.split(" ")
        if int(number) > max[color]:
            max[color] = int(number)
    return max


def is_possible(line, max):
    line_max = get_max_in_line(line)
    is_possible = True
    for color in line_max.keys():
        if line_max[color] > max[color]:
            is_possible = False
    return is_possible


def get_total(input, max):
    total = 0
    for line in input:
        if (is_possible(line, max) == True):
            total += get_id_from_line(line)
    return total

def get_power(input):
    total_power = 0
    for line in input:
        line_power = 1
        line_max = get_max_in_line(line)
        for value in line_max.values():
            line_power *= value
        total_power += line_power
    return total_power

print(get_total(input, { "red": 12, "green": 13, "blue": 14}))
print(get_power(input))