def prepare_puzzle(puzzle):
    return [parse_exp(exp.replace(' ', '')) for exp in puzzle]

def parse_exp(exp):
    result = []
    i = 0
    while i < len(exp):
        if exp[i] == '(':
            i, exp_start, open_parentheses = i+1, i+1, 0
            while exp[i] != ')' or open_parentheses > 0:
                if exp[i] == ')':   open_parentheses -= 1
                elif exp[i] == '(': open_parentheses += 1
                i += 1
            result.append(parse_exp(exp[exp_start:i]))
        else:
            result.append(exp[i])
        i += 1    
    return result

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def is_leaf(self):
        return self.left == None and self.right == None

def construct_tree(expression):
    i, operator = len(expression) -1, None
    while i >= 0:
        if isinstance(expression[i], str) and expression[i] in '+*':
            operator = expression[i]
            i -= 1
        else:
            if isinstance(expression[i], list): node = construct_tree(expression[i])
            elif operator == None: node = Node(int(expression[i]))
            if operator == None:
                right_node = node
                i -= 1
            else:
                root = Node(operator)
                root.left = construct_tree(expression[:i+1])
                root.right = right_node
                operator = None
                return root
    return node

def eval_exp(root):
    if root.is_leaf():
        return root.value
    if root.value == '+':
        return eval_exp(root.left) + eval_exp(root.right)
    if root.value == '*':
        return eval_exp(root.left) * eval_exp(root.right)

def insert_parenteses(exp):
    i = 0
    while i < len(exp):
        if exp[i] == '+':
            new_exp = [exp[i-1], exp[i], insert_parenteses(exp[i+1])]
            del exp[i:i+2]
            exp[i-1] = new_exp
        else:
            if isinstance(exp[i], list): exp[i] = insert_parenteses(exp[i])
            i += 1
    return exp

def sum_eval_all(expressions):
    return sum([eval_exp(tree) for tree in [construct_tree(exp) for exp in expressions]])

def solve_part1(puzzle):
    return sum_eval_all(puzzle)

def solve_part2(puzzle):
    return sum_eval_all([insert_parenteses(exp) for exp in puzzle])
