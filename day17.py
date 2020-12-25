import itertools

def prepare_puzzle(puzzle):
    return set((x, y, 0, 0) for (y, line) in enumerate(puzzle) for x, cube in enumerate(line) if cube == '#')

ln = list(itertools.product([-1, 0, 1], repeat=4))
ln.remove((0, 0, 0, 0))
def count_neighbors(cubes, x, y, z, w):
    return sum([1 for x1, y1, z1, w1 in ln if (x+x1, y+y1, z+z1, w+w1) in cubes])

lf = list(itertools.product([-1, 0, 1], repeat=4))
def proceed_cycle(cubes, is3d = False):
    new_cubes = set()
    for x, y, z, w in cubes:
        for x1, y1, z1, w1 in lf:
            nx, ny, nz, nw = x+x1, y+y1, z+z1, w+w1
            if (nx, ny, nz, nw) not in new_cubes:
                if is3d: nw = 0
                neighbors = count_neighbors(cubes, nx, ny, nz, nw)
                if (nx, ny, nz, nw) in cubes:
                    if neighbors in [2, 3]: new_cubes.add((nx, ny, nz, nw))
                elif neighbors == 3:        new_cubes.add((nx, ny, nz, nw))
    return new_cubes

def solve_part1(puzzle):
    for _ in range(6): puzzle = proceed_cycle(puzzle, True)
    return len(puzzle)

def solve_part2(puzzle):
    for _ in range(6): puzzle = proceed_cycle(puzzle)
    return len(puzzle)
