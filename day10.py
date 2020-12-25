def prepare_puzzle(puzzle):
    puzzle = [int(n) for n in puzzle]
    puzzle.sort()
    return [0] + puzzle + [puzzle[-1] + 3]

def solve_part1(puzzle):
    l = [puzzle[i+1] - n for i, n in enumerate(puzzle[:-1])]
    return l.count(1) * l.count(3)

helper = {}
def get_arrangements(puzzle, i):
    if i+1 == len(puzzle): return 1
    if i in helper: return helper[i]
    helper[i] = sum([get_arrangements(puzzle, i+n) for n in [1, 2, 3]
                        if i+n < len(puzzle) and puzzle[i+n] - puzzle[i] <= 3])
    return helper[i]

def solve_part2(puzzle):
    return get_arrangements(puzzle, 0)
