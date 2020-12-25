def prepare_puzzle(puzzle):
    p = [(len(puzzle[0])+2) * ['x']]
    return p + [['x'] + list(x) + ['x'] for x in puzzle] + p

def count_occupied_seats(seat_layout, star):
    temp = [['x' for _ in seat_layout[0]] for _ in seat_layout]
    while seat_layout != temp:
        people_arrive(seat_layout, temp, star)
        seat_layout, temp = temp, seat_layout
    return sum([l.count('#') for l in seat_layout])

def people_arrive(seat_layout, temp, star):
    for y, row in enumerate(seat_layout[1:-1]):
        for x, seat in enumerate(row[1:-1]):
            if seat == 'L' and adj_seats(seat_layout, x+1, y+1, star) == 0:
                seat = '#'
            elif seat == '#' and adj_seats(seat_layout, x+1, y+1, star) >= (4 if star == 1 else 5):
                seat = 'L'
            temp[y+1][x+1] = seat

adj = [lambda x, y, n: (x-n, y-n), lambda x, y, n: (x, y-n), lambda x, y, n: (x+n, y-n),
        lambda x, y, n: (x-n, y), lambda x, y, n: (x+n, y),
        lambda x, y, n: (x-n, y+n), lambda x, y, n: (x, y+n), lambda x, y, n: (x+n, y+n)]

def adj_seats(seat_layout, x, y, star):
    result = 0
    for f in adj:
        seat = '.'
        if star == 1:
            tx, ty = f(x, y, 1)
            seat = seat_layout[ty][tx]
        else:
            n = 1
            while seat == '.':
                tx, ty = f(x, y, n)
                seat = seat_layout[ty][tx]
                n += 1
        if seat == '#':
            result += 1
    return result

def solve_part1(puzzle):
    return count_occupied_seats(puzzle, 1)

def solve_part2(puzzle):
    return count_occupied_seats(puzzle, 2)
