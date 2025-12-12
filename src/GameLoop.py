def print_board(board):
    print("\n")
    for i in range (3):

        # Slices the board into three row (0,1,2) (3,4,5) (6,7,8)
        row = board[i*3:(i+1)*3] 

        # Concat | with the strings if they are not empty else put space in the empty string " "
        print(" | ".join(cell if cell != "" else " " for cell in row)) 

        #print separator after first two rows
        if i < 2:
            print ("----------") 

        # print ("\n")

def check_winner (board):
    win_states = [
        (0,1,2), (3,4,5), (6,7,8), # rows
        (0,3,6), (1,4,7), (2,5,8), # columns
        (0,4,8), (2,4,6)           # diagonals
    ]
    for a, b, c in win_states:
        if board[a] != "" and board[a] == board[b] == board[c]:
            return board[a] #return "X" or "O" (winner)
        
        
    if "" not in board: # if there is no empty spaces then Tie
            return "Tie"
        
    return None # game continues


def ai_move_decider(board, ai_symbol):
    '''
    This function is used to make the ai plays his move,
    it should use Minimax algorithm ,

    but for now it will return any valid move 
    '''
    import random

    #enumerate(board) return (index, value) if v is empty then i is valid
    valid_moves = [i for i, v in enumerate(board) if v == ""]

    return random.choice(valid_moves)


def game_loop (player_symbol = "X", ai_symbol="O"):
    board = [""] * 9
    current = "X" # First to play 

    print ("Starting Tic-Tac-Toe")
    print(board)

    while True:
        if current == player_symbol:
            move = -1
            valid = [i for i, v in enumerate(board) if v == ""]

            while move not in valid:
                try:
                    move = int(input("Enter you move (0-8): "))
                except ValueError:
                    continue
        
            board[move] = player_symbol
        
        else:
            print("Ai turn")

            move = ai_move_decider(board, ai_symbol)
            board[move] = ai_symbol

        print_board(board)

        # check if game ends
        result = check_winner(board)
        if result == "Tie":
            print ("The game ends with draw")
            break
        elif result is not None:
            print ("Winner is " + result)
            break

        current = "O" if current == "X" else "X"



#Run the game 
game_loop()


