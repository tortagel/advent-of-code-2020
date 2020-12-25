import math

def parse_range(r):
    return (int(r[:r.find('-')]), int(r[r.find('-')+1:]))

def prepare_puzzle(puzzle):
    i, rules = 0, []
    while puzzle[i] != '':
        rules.append((puzzle[i][:puzzle[i].find(':')],
          parse_range(puzzle[i][puzzle[i].find(':')+2:puzzle[i].find(' or ')]),
          parse_range(puzzle[i][puzzle[i].find(' or ')+4:])))
        i += 1
    your_ticket = [int(n) for n in puzzle[i+2].split(',')]
    nearby_tickets = [[int(n) for n in line.split(',')] for line in puzzle[i+5:]]
    return (rules, your_ticket, nearby_tickets)

def validate_tickets(rules, nearby_tickets):
    error_rate, valid_tickets = 0, []
    for nearby_ticket in nearby_tickets:
        error = sum([value for value in nearby_ticket
                        if all([(value < from1 or value > to1) and (value < from2 or value > to2)
                                    for _, (from1, to1), (from2, to2) in rules])])
        if error > 0: error_rate += error
        else: valid_tickets.append(nearby_ticket)
    return valid_tickets, error_rate

def solve_part1(puzzle):
    rules, _, nearby_tickets = puzzle
    _, error_rate = validate_tickets(rules, nearby_tickets)
    return error_rate

def solve_part2(puzzle):
    rules, your_ticket, nearby_tickets = puzzle
    valid_tickets, _ = validate_tickets(rules, nearby_tickets)
    ticket_fields = {}
    for field in range(len(valid_tickets[0])):
        for name, (from1, to1), (from2, to2) in rules:
            if all([(x >= from1 and x <= to1) or (x >= from2 and x <= to2)
                        for x in [ticket[field] for ticket in valid_tickets]]):
                if name in ticket_fields: ticket_fields[name].append(field)
                else: ticket_fields[name] = [field]
    field_pos = []
    for _ in range(len(valid_tickets[0])):
        name, field = [(name, fields[0]) for name, fields in ticket_fields.items() if len(fields) == 1][0]
        field_pos.append((field, name))
        ticket_fields = {name: [f for f in fields if f != field] for name, fields in ticket_fields.items() }
    return math.prod([your_ticket[field] for field, name in field_pos if name.startswith('departure')])
