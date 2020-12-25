import ast

def prepare_puzzle(puzzle):
    return [exp.replace('*', '-') for exp in puzzle]

def eval_part1(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node.op, ast.Add):
        return eval_part1(node.left) + eval_part1(node.right)
    elif isinstance(node.op, ast.Sub):
        return eval_part1(node.left) * eval_part1(node.right)

def eval_part2(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node.op, ast.Add):
        return eval_part2(node.left) * eval_part2(node.right)
    elif isinstance(node.op, ast.Mult):
        return eval_part2(node.left) + eval_part2(node.right)

def solve_part1(puzzle):
    return sum([eval_part1(ast.parse(exp, mode='eval').body) for exp in puzzle])

def solve_part2(puzzle):
    puzzle = [exp.replace('+', '*').replace('-', '+') for exp in puzzle]
    return sum([eval_part2(ast.parse(exp, mode='eval').body) for exp in puzzle])
