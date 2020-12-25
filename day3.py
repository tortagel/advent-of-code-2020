def prepare_puzzle(puzzle):
    return puzzle

def count_trees(puzzle, right, down = 1):
    trees = 0
    n = 0
    for line in puzzle[1::down]:
        n += right
        n %= len(line)
        if line[n] == '#':
            trees += 1
    return trees

def solve_part1(puzzle):
    return count_trees(puzzle, 3)

def solve_part2(puzzle):
    result = count_trees(puzzle, 1)
    result *= count_trees(puzzle, 3)
    result *= count_trees(puzzle, 5)
    result *= count_trees(puzzle, 7)
    result *= count_trees(puzzle, 1, 2)
    return result
