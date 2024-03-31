#!/usr/bin/env python3

import sys

def alpha_beta_minmax(game_state, depth, alpha, beta, maximizing_player, version):
    # Terminal condition: One of the piles is empty or depth limit reached
    if game_state['num_red'] == 0 or game_state['num_blue'] == 0 or depth == 0:
        return evaluate_state(game_state, version, maximizing_player), None

    if maximizing_player:
        max_eval = float('-inf')
        best_move = None
        for move in get_possible_moves(game_state):
            new_game_state = game_state.copy()
            apply_move(new_game_state, move)
            eval, _ = alpha_beta_minmax(new_game_state, depth - 1 if depth is not None else None, alpha, beta, False, version)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = float('inf')
        best_move = None
        for move in get_possible_moves(game_state):
            new_game_state = game_state.copy()
            apply_move(new_game_state, move)
            eval, _ = alpha_beta_minmax(new_game_state, depth - 1 if depth is not None else None, alpha, beta, True, version)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

def evaluate_state(game_state, version, maximizing_player):
    base_score = 2 * game_state['num_red'] + 3 * game_state['num_blue']
    if version == 'misere':
        return base_score if maximizing_player else -base_score
    else:  # standard
        return -base_score if maximizing_player else base_score

def calculate_score(game_state, version):
    if version == 'misere':
        return -(2 * game_state['num_red'] + 3 * game_state['num_blue'])
    else:  # standard
        return (2 * game_state['num_red'] + 3 * game_state['num_blue'])

def apply_move(game_state, move):
    game_state[f'num_{move[0]}'] = max(0, game_state[f'num_{move[0]}'] - move[1])

def get_possible_moves(game_state):
    moves = []
    if game_state['num_red'] >= 2:
        moves.append(('red', 2))
    if game_state['num_blue'] >= 2:
        moves.append(('blue', 2)) 
    if game_state['num_red'] >= 1:
        moves.append(('red', 1))
    if game_state['num_blue'] >= 1:
        moves.append(('blue', 1))
    return moves

def main(num_red, num_blue, version, first_player, depth):
    game_state = {
        'num_red': num_red,
        'num_blue': num_blue,
    }

    current_player = first_player

    acc = 0 # accumulator
    while game_state['num_red'] > 0 and game_state['num_blue'] > 0:
        print(f"[{acc}] Current state:"); acc += 1
        print(f"\tRed marbles: {game_state['num_red']}\n\tBlue marbles: {game_state['num_blue']}")
        if current_player == 'computer':
            _, move = alpha_beta_minmax(game_state, depth, float('-inf'), float('inf'), True, version)
            print(f"Computer chooses to remove {move[1]} marble(s) from the {move[0]} pile.", end="\n\n")
            apply_move(game_state, move)
        else:
            valid_move = False
            while not valid_move:
                try:
                    pile = input("Choose a pile (red/blue): ").strip().lower()
                    amount = int(input("Choose the amount (1/2): "))
                    print(end="\n\n")
                    if (pile in ['red', 'blue']) and amount in [1, 2] and game_state[f'num_{pile}'] >= amount:
                        valid_move = True
                        apply_move(game_state, (pile, amount))
                    else:
                        print("Invalid move, try again.")
                except ValueError:
                    print("Invalid input, try again.")
        
        current_player = 'human' if current_player == 'computer' else 'computer'
    
    score = calculate_score(game_state, version)
    match version:
        case 'standard':
            winner = 'computer' if current_player == 'human' else 'human'
        case 'misere':
            winner = 'human' if current_player == 'human' else 'computer'

    print(f"{winner.capitalize()} wins. Final score: {abs(score)}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: red_blue_nim.py <num-red> <num-blue> [<version>] [<first-player>] [<depth>]")
        sys.exit(1)

    num_red = int(sys.argv[1])
    num_blue = int(sys.argv[2])
    version = 'standard' if len(sys.argv) < 4 else sys.argv[3]
    first_player = 'computer' if len(sys.argv) < 5 else sys.argv[4]
    depth = None if len(sys.argv) < 6 else int(sys.argv[5])

    main(num_red, num_blue, version, first_player, depth)
