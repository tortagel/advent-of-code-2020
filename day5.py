def prepare_puzzle(puzzle):
    plane = [[0 for _ in range(8)] for _ in range(128)]
    for seat in puzzle:
        row = binary_search([x == 'F' for x in seat[:7]])
        col = binary_search([x == 'L' for x in seat[7:]])
        plane[row][col] = row * 8 + col
    return plane

def binary_search(part):
    l = list(range(2 ** len(part)))
    for x in part:
        idx = len(l) // 2
        l = l[:idx] if x else l[idx:]
    return l[0]

def solve_part1(puzzle):
    return max(map(max, puzzle))

def solve_part2(puzzle):
    for i in range(1, 8 * len(puzzle)):
        if puzzle[(i-1)//8][(i-1)%8] > 0 and puzzle[i//8][i%8] == 0 and puzzle[(i+1)//8][(i+1)%8] > 0:
            return (i//8) * 8 + (i%8)
