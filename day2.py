# 2-6 w: wkwwwfwwpvw
def prepare_puzzle(puzzle):
    l = []
    for temp in puzzle:
        pos1 = temp.find('-')
        pos2 = temp.find(' ')
        pos3 = temp.find(':')
        f = int(temp[:pos1])
        t = int(temp[pos1+1:pos2])
        b = temp[pos2+1:pos3]
        p = temp[pos3+1:].strip()
        l.append([f, t, b, p])
    return l

def solve_part1(puzzle):
    count = 0
    for temp in puzzle:
        c = temp[3].count(temp[2])
        if c >= temp[0] and c <= temp[1]:
            count += 1
    return count

def solve_part2(puzzle):
    count = 0
    for temp in puzzle:
        if (temp[3][temp[0]-1] == temp[2]) != (temp[3][temp[1]-1] == temp[2]):
            count += 1
    return count
