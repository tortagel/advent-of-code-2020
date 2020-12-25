from collections import Counter
from itertools import groupby

def prepare_puzzle(puzzle):
    return list(map(lambda x: [len(x), ''.join(x)], [list(g) for k, g in groupby(puzzle, lambda x: x != '') if k]))

def solve_part1(puzzle):
    return sum([len(set(group[1])) for group in puzzle])

def solve_part2(puzzle):
    return sum([len([v for _, v in Counter(group[1]).items() if v == group[0]]) for group in puzzle])
