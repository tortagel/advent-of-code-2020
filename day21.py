def prepare_puzzle(puzzle):
    return [(set(food[:food.find('(')-1].split(' ')), food[food.find('(')+10:-1].split(', ')) for food in puzzle]

def solve_part1(puzzle):
    temp = dict()
    all_ingredients = []
    for food in puzzle:
        ingredients, allergens = food
        all_ingredients += ingredients
        for allergen in allergens:
            if allergen in temp:
                temp[allergen].append(ingredients)
            else:
                temp[allergen] = [ingredients]
    for allergen, foods in temp.items():
        temp[allergen] = set.intersection(*map(set,foods))
    for ingredient in set.union(*temp.values()):
        all_ingredients = list(filter(lambda x: x != ingredient, all_ingredients))
    return len(all_ingredients)

def solve_part2(puzzle):
    temp = dict()
    for food in puzzle:
        ingredients, allergens = food
        for allergen in allergens:
            if allergen in temp:
                temp[allergen].append(ingredients)
            else:
                temp[allergen] = [ingredients]
    for allergen, foods in temp.items():
        temp[allergen] = set.intersection(*map(set,foods))
    result = []
    while len(temp) > 0:
        allergen, ingredient = [(allergen, list(ingredients)[0]) for allergen, ingredients in temp.items() if len(ingredients) == 1][0]
        result.append((allergen, ingredient))
        del temp[allergen]
        for a, f in temp.items():
            if ingredient in f:
                temp[a].remove(ingredient)
    result.sort(key = lambda tup: tup[0])
    return ','.join([ingredient for _, ingredient in result])
