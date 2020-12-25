def prepare_puzzle(puzzle):
    tiles = []
    for line in puzzle:
        i, tile = 0, []
        while i < len(line):
            if line[i:i+1] in ['e', 'w']:
                tile.append(line[i:i+1])
                i += 1
            elif line[i:i+2] in ['se', 'sw', 'nw', 'ne']:
                tile.append(line[i:i+2])
                i += 2
        tiles.append(tile)
    return tiles

def create_floor(tiles):
    floor = {}
    for tile in tiles:
        x, y = 0, 0
        for direction in tile:
            x, y = adjacent_tiles(x, y)[direction]
        floor[(x, y)] = not floor.get((x, y), False)
    return floor

def solve_part1(puzzle):
    floor = create_floor(puzzle)
    return list(floor.values()).count(True)

def add_white_adjacents(floor):
    for x, y in [(x, y) for (x, y), is_black in floor.items() if is_black]:
        for tx, ty in adjacent_tiles(x, y).values():
            floor[(tx, ty)] = floor.get((tx, tx), False)

def adjacent_tiles(x, y):
    return {'e': (x+1, y-1), 'se': (x, y-1), 'sw': (x-1, y), 'w': (x-1, y+1), 'nw': (x, y+1), 'ne': (x+1, y)}

def flip_floor(floor, new_floor):
    add_white_adjacents(floor)
    for (x, y), is_black in floor.items():
        black_adjacents = [floor.get((tx, ty), False) for tx, ty in adjacent_tiles(x, y).values()].count(True)
        if is_black and black_adjacents == 0 or black_adjacents > 2:
            new_floor[(x, y)] = False
        elif not is_black and black_adjacents == 2:
            new_floor[(x, y)] = True
        else:
            new_floor[(x, y)] = is_black
    return new_floor

def solve_part2(puzzle):
    floor, temp = create_floor(puzzle), {}
    for _ in range(100):
        flip_floor(floor, temp)
        floor, temp = temp, floor
    return list(floor.values()).count(True)
