def prepare_puzzle(puzzle):
    prog, temp = [], []
    for line in puzzle:
        if line[:4] == 'mask':
            temp = [[(len(line[7:])-i-1, int(b) if b != 'X' else -1) for i, b in enumerate(line[7:])], []]
            prog.append(temp)
        else:
            temp[1].append((int(line[4:line.find(']')]), int(line[line.find('=')+1:])))
    return prog

def set_bit(value, i, bit):
    if bit == 0:
        value &= ~(1<<i)
    elif bit == 1:
        value |= (1<<i)
    return value

def solve_part1(puzzle):
    mem = {}
    for mask, instructions in puzzle:
        for addr, value in instructions:
            for i, b in mask:
                value = set_bit(value, i, b)
            mem[addr] = value
    return sum(mem.values())

def solve_part2(puzzle):
    mem = {}
    for mask, instructions in puzzle:
        for addr, value in instructions:
            for i, b in mask:
                if b == 1:
                    addr |= (1<<i)
            floating = [i for i, b in mask if b == -1]
            for f in list(range(2**len(floating))):
                for i, b in enumerate(floating):
                    addr = set_bit(addr, b, (f>>i) & 1)
                    mem[addr] = value
    return sum(mem.values())
