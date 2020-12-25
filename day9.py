def prepare_puzzle(puzzle):
    return [int(n) for n in puzzle]

def solve_part1(puzzle):
    for idx, n in enumerate(puzzle[25:]):
        if n not in [n1 + n2 for n2 in puzzle[idx:idx+25] for n1 in puzzle[idx:idx+25]]:
            return n

def solve_part2(puzzle):
    target_sum = solve_part1(puzzle)
    start, stop, current_sum = 0, 0, 0
    while stop < len(puzzle):
        if current_sum == target_sum:
            return min(puzzle[start:stop]) + max(puzzle[start:stop])
        elif current_sum > target_sum:
            current_sum -= puzzle[start]
            start += 1
        else:
            current_sum += puzzle[stop]
            stop += 1
