from copy import deepcopy
import importlib
import argparse
import time

def parse_puzzle(day):
    filename = f'input\\day{day}.txt'
    with open(filename, 'r') as file:
        puzzle = file.readlines()
        puzzle = [x.strip() for x in puzzle]
        return puzzle

def solve(day, part, with_time):
    try:
        solver = importlib.import_module(f'day{day}')
    except ModuleNotFoundError:
        print(f'No solver script available for day \'{day}\'!')
        return
    if part != None and (part < 1 or part > 2):
        print(f'Part \'{part}\' is not valid!')
        return
    t0 = time.time()
    puzzle = parse_puzzle(day)
    puzzle = solver.prepare_puzzle(puzzle)
    t1 = time.time()
    if with_time:
        print(f'parsed in {t1-t0} sec')
    if part == None or part == 1:
        t0 = time.time()
        result = solver.solve_part1(deepcopy(puzzle))
        t1 = time.time()
        print(f'part 1: {result}' + (f' in {t1-t0} sec' if with_time else ''))
    if part == None or part == 2:
        t0 = time.time()
        result = solver.solve_part2(deepcopy(puzzle))
        t1 = time.time()
        print(f'part 2: {result}' + (f' in {t1-t0} sec' if with_time else ''))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('day', type=int, help='day between 1 and 24')
    parser.add_argument('-p', '--part',  type=int, default=None, help='part (default: part 1 and 2)')
    parser.add_argument('-t', '--time',  action='store_true', help='with time output (default: False)')
    args = parser.parse_args()
    solve(args.day, args.part, args.time)

if __name__ == '__main__':
	main()
