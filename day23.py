def prepare_puzzle(puzzle):
    return [int(n) for n in puzzle[0]]

def move_cups(puzzle, moves):
    cups = {n: puzzle[i+1] if i+1 < len(puzzle) else puzzle[0] for i, n in enumerate(puzzle)}
    current_cup = puzzle[0]
    for _ in range(moves):
        cup1 = cups[current_cup]
        cup2 = cups[cup1]
        cup3 = cups[cup2]
        cups[current_cup] = cups[cup3]
        destination = current_cup - 1
        while destination in [0, cup1, cup2, cup3]:
            destination = max(puzzle) if destination < 1 else destination - 1
        cups[cup3] = cups[destination]
        cups[destination] = cup1
        current_cup = cups[current_cup]
    return cups

def solve_part1(puzzle):
    cups = move_cups(puzzle, 100)
    result = ''
    cup = cups[1]
    while cup != 1:        
        result += str(cup)
        cup = cups[cup]
    return result

def solve_part2(puzzle):
    temp = puzzle + list(range(max(puzzle)+1, 1000001))
    cups = move_cups(temp, 10000000)
    return cups[1] * cups[cups[1]]
