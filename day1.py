def prepare_puzzle(puzzle):
    return [int(n) for n in puzzle]

def solve_part1(puzzle):
    for n1 in puzzle:
        for n2 in puzzle:
            if n1 + n2 == 2020:
                return n1 * n2

def solve_part2(puzzle):
    for n1 in puzzle:
        for n2 in puzzle:
            for n3 in puzzle:
                if n1 + n2 + n3 == 2020:
                    return n1 * n2 * n3
