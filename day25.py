def prepare_puzzle(puzzle):
    return (int(puzzle[0]), int(puzzle[1]))

def reverse_loop_size(pup_key):
    loop_size, temp = 0, 1
    while pup_key != temp:
        temp = (temp * 7) % 20201227
        loop_size += 1
    return loop_size

def solve_part1(puzzle):
    pup_key1, pup_key2 = puzzle
    return pow(pup_key1, reverse_loop_size(pup_key2), 20201227)

def solve_part2(puzzle):
    return None
