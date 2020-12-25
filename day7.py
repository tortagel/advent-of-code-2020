def prepare_puzzle(puzzle):
    bags = {}
    for rule in puzzle:
        pos = rule.find(' bags contain ')
        bags[rule[:pos]] = []
        for bag in rule[pos+14:-1].split(', '):
            count = bag[:bag.find(' ')]
            if count != 'no':
                bags[rule[:pos]].append([int(count), bag[bag.find(' ')+1:bag.rfind(' ')]])
    for _, v in bags.items():
        for bag in v:
            bag[1] = [bag[1], bags[bag[1]]]
    return bags

def contains_bag(bags, bag_name):
    for bag in bags:
        if bag[1][0] == bag_name or contains_bag(bag[1][1], bag_name):
            return True
    return False

def solve_part1(puzzle):
    return sum([1 for _, v in puzzle.items() if contains_bag(v, 'shiny gold')])

def count_bags(bags):
    return sum([bag[0] + bag[0] * count_bags(bag[1][1]) for bag in bags])

def solve_part2(puzzle):
    return count_bags(puzzle['shiny gold'])
