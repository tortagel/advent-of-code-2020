import regex as re

def prepare_puzzle(puzzle):
    i, rules = 0, {}
    while puzzle[i] != '':
        temp = puzzle[i].split(':')
        rules[int(temp[0])] = []
        if '"' in temp[1]:
            rules[int(temp[0])] = temp[1][2:3]
        else:
            rules[int(temp[0])] = [[int(n) for n in s.strip().split(' ')] for s in temp[1].split('|')]
        i += 1
    rules[8].append([42, 'R8'])
    rules[11].append([42, 'R11', 31])
    for v in rules.values():
        if isinstance(v, list):
            for k, rule in enumerate(v):
                for j, n in enumerate(rule):
                    if n in ['R8', 'R11']:
                        rule[j] = n
                    else:
                        rule[j] = rules[n]
                if all([isinstance(x, str) for x in rule]):
                    v[k] = ''.join(v[k])
    return (rules[0][0], puzzle[i+1:])

def build_regex(rules, recursive = False):
    regex = ''
    for x in rules:
        if isinstance(x, list):
            regex += '(' + '|'.join([build_regex(r, recursive) for r in x]) + ')'
        elif x == 'R8':
            regex += '(?1)' if recursive else ''
        elif x == 'R11':
            regex += '(???)' if recursive else ''
        else:
            regex += x
    return regex

def count_sub_pattern(regex):
    i = open_parentheses = sub_pattern = 1
    while open_parentheses > 0:
        if regex[i] == ')':
            open_parentheses -= 1
        elif regex[i] == '(':
            open_parentheses += 1
            sub_pattern += 1
        i += 1
    return sub_pattern

def solve_part1(puzzle):
    rules, messages = puzzle
    r = re.compile(f'^{build_regex(rules)}$')
    return len([m for m in messages if r.match(m)])

def solve_part2(puzzle):
    rules, messages = puzzle
    regex = build_regex(rules, recursive = True)
    regex = regex.replace('(???)', f'(?{count_sub_pattern(regex)})')
    r = re.compile(f'^{regex}$')
    return len([m for m in messages if r.match(m)])
