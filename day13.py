import math

def prepare_puzzle(puzzle):
    return (int(puzzle[0]), [(int(n), i) for i, n in enumerate(puzzle[1].split(',')) if n != 'x'])

def solve_part1(puzzle):
    start_time, buses = puzzle
    bus, next_start = min([(bus, start_time + bus - (start_time % bus)) for bus, _ in buses], key=lambda x: x[1])
    return (next_start - start_time) * bus

def solve_part2(puzzle):
    _, buses = puzzle
    t, n = 0, 1
    for bus, offset in buses:
        while (t + offset) % bus != 0:
            t += n
        n *= bus
    return t
