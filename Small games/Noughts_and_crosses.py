wins = [
    '111 000 000', '000 111 000', '000 000 111',    # Across
    '100 100 100', '010 010 010', '001 001 001',    # Down
    '100 010 001', '001 010 100',                   # Diagonal
]
# Store winning boards as integers
wins = [int(w.replace(' ', ''), 2) for w in wins]


# Returns True if board is a winning position
winning_board = lambda b: any((b & w) == w for w in wins)


# Makes a move. Returns new board.
# N.B. 1 << m is much faster than pow(2, m). Important for this game...
make_move = lambda m, b: (1 << m) | b


def illegal_move(move, game):
    """Returns name of player if they already made the move, else None."""
    for player in game:
        if make_move(move, game[player]) == game[player]:
            return player


def new_game():
    # The game is represented as 2 boards, 1 for each player, where the value
    # is stored as an integer but you can think of it as a 9-digit binary number.
    game = {'X': 0, 'O': 0}
    print("Noughts and crosses, but you get to play both sides...")
    print_game(game)

    # X goes first. Maximum of 9 moves.
    for player in 'XOXOXOXOX':
        move = prompt(player)
        while illegal_move(move, game):
            move = prompt(player)
        
        game[player] = make_move(move, game[player])
    
        print_game(game)

        if winning_board(game[player]):
            print("%s wins!" % player)
            break
    else:
        print("Game ends with a draw.")
    

def prompt(player):
    """Prompts for a number between 1 and 9. Returns an int between 0 and 8."""
    while True:
        line = input("%s to play. Enter a number between 1 - 9: " % player)
        try:
            move = int(line.strip())
            if 1 <= move <= 9:
                # Subtract 1 because the boards are zero-based.
                return move - 1
        except ValueError:
            pass
        
        
def print_game(game):
    """Prints the board with X and O for player 1 and 2 respectively, and a
    digit for each free position.
    """
    board = [illegal_move(x, game) or str(x + 1) for x in range(9)]
    print( '\n' + '\n'.join(' '.join(board[x:x + 3]) for x in (0, 3, 6)) + '\n')
