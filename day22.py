def prepare_puzzle(puzzle):
    puzzle = [int(n) for n in puzzle[1:] if n not in ['', 'Player 2:']]
    return (puzzle[:len(puzzle)//2], puzzle[len(puzzle)//2:])

def solve_part1(puzzle):
    player1, player2 = puzzle
    while len(player1) > 0 and len(player2) > 0:
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 > card2: player1 += [card1, card2]
        else: player2 += [card2, card1]
    winner = player1 if len(player1) > 0 else player2
    return sum([(i+1) * card for i, card in enumerate(reversed(winner))])

def recursion_compat(player1, player2, history1, history2):
    while len(player1) > 0 and len(player2) > 0:
        if player1 in history1 or player2 in history2:
            player2.clear()
            break
        history1.append(player1.copy())
        history2.append(player2.copy())
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if len(player1) >= card1 and len(player2) >= card2:
            rec_player1, rec_player2 = player1[:card1].copy(), player2[:card2].copy()
            recursion_compat(rec_player1, rec_player2, [], [])
            if len(rec_player1) > 0: player1 += [card1, card2]
            else: player2 += [card2, card1]
        elif card1 > card2: player1 += [card1, card2]
        else: player2 += [card2, card1]

def solve_part2(puzzle):
    player1, player2 = puzzle
    recursion_compat(player1, player2, [], [])
    winner = player1 if len(player1) > 0 else player2
    return sum([(i+1) * card for i, card in enumerate(reversed(winner))])
