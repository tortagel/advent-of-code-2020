#acc +13
def prepare_puzzle(puzzle):
    return [[inst[:3], int(inst[4:])] for inst in puzzle]

class InfiniteLoopError(Exception):
    pass

class Interpreter:

    def __init__(self, boot_code):
        self.boot_code = boot_code
        self.inst_counter = 0
        self.accumulator = 0
        self.inst_history = []

    def run(self):
        while self.inst_counter < len(self.boot_code):
            self.check_for_infinite_loop()
            op = self.boot_code[self.inst_counter][0]
            arg = self.boot_code[self.inst_counter][1]
            if op == 'acc':
                self.accumulator += arg
                self.inst_counter += 1
            elif op == 'jmp':
                self.inst_counter += arg
            elif op == 'nop':
                self.inst_counter += 1
        return self.accumulator
    
    def check_for_infinite_loop(self):
        if self.inst_counter in self.inst_history:
            raise InfiniteLoopError(self.accumulator)
        self.inst_history.append(self.inst_counter)            

def solve_part1(puzzle):
    interpreter = Interpreter(puzzle)
    try:
        interpreter.run()
    except InfiniteLoopError as err:
        return err.args[0]

def repair_inst(inst):
    if inst[0] == 'jmp':
        inst[0] = 'nop'
    elif inst[0] == 'nop':
        inst[0] = 'jmp'
    else:
        return False
    return True

def solve_part2(puzzle):
    for inst in puzzle:
        if repair_inst(inst):
            interpreter = Interpreter(puzzle)
            try:
                return interpreter.run()
            except InfiniteLoopError:
                repair_inst(inst) # revert repair
