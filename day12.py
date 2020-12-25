import math

def prepare_puzzle(puzzle):
    return [(x[:1], int(x[1:])) for x in puzzle]

def solve_part1(puzzle):
    x, y, direction = 0, 0, 0
    for action, value in puzzle:
        if action == 'N':   y += value
        elif action == 'S': y -= value
        elif action == 'E': x += value
        elif action == 'W': x -= value
        elif action == 'L': direction = (direction + value) % 360
        elif action == 'R': direction = (direction - value) % 360
        elif action == 'F':
            x += int(math.cos(math.radians(direction)) * value)
            y += int(math.sin(math.radians(direction)) * value)
    return abs(x) + abs(y)

def solve_part2(puzzle):
    x, y, wx, wy = 0, 0, 10, 1
    for action, value in puzzle:
        if action == 'N':   wy += value
        elif action == 'S': wy -= value
        elif action == 'E': wx += value
        elif action == 'W': wx -= value
        elif action == 'L':
            if value == 90:    wx, wy = -wy, wx
            elif value == 180: wx, wy = -wx, -wy
            elif value == 270: wx, wy = wy, -wx
        elif action == 'R':
            if value == 90:    wx, wy = wy, -wx
            elif value == 180: wx, wy = -wx, -wy
            elif value == 270: wx, wy = -wy, wx
        elif action == 'F':
            x += value * wx
            y += value * wy
    return abs(x) + abs(y)
