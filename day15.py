def prepare_puzzle(puzzle):
    return [int(n) for n in puzzle[0].split(',')]

def get_number_spoken(puzzle, nth):
    history = {n: i+1 for i, n in enumerate(puzzle)}
    last_number = puzzle[-1]
    prev_number = -1
    for turn in range(len(puzzle)+1, nth+1):
        last_number = 0 if prev_number == -1 else (turn-1) - prev_number
        prev_number = history[last_number] if last_number in history else -1
        history[last_number] = turn
    return last_number

def solve_part1(puzzle):
    return get_number_spoken(puzzle, 2020)

def solve_part2(puzzle):
    return get_number_spoken(puzzle, 30000000)
