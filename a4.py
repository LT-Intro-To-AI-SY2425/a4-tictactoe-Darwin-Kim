# NOTE: Until you fill in the TTTBoard class mypy is going to give you multiple errors
# talking about unimplemented class attributes, don't worry about this as you're working


class TTTBoard:
    """A tic tac toe board

    Attributes:
        board - a list of '*'s, 'X's & 'O's. 'X's represent moves by player 'X', 'O's
            represent moves by player 'O' and '*'s are spots no one has yet played on
    """
    def __init__(self):
        global board
        board=["*","*","*","*","*","*","*","*","*"]

    def __str__(self):
        global board
        boardStr=str(board[0:3])+"\n"+str(board[3:6])+"\n"+str(board[6:9])
        return boardStr

    def make_move(self, player, pos):
        # VARIABLES
        global board

        # Checking if the position on the board exists and is set to "*", then making the move if it is
        if pos in range(len(board)) and board[pos]=="*":
            board[pos]=player
        return True if pos<len(board) and board[pos]==player else False
    
    def has_won(self,player):
        # VARIABLES
        global board
        Won=False
        possibleWins=[[0,4,8],[6,4,2],         # DIAGONALS
                      [0,1,2],[3,4,5],[6,7,8], # STRAIGHT ACROSS
                      [0,3,6],[1,4,7],[2,5,8]] # STRAIGHT DOWN
        
        # Checking possibleWins for matches
        for i in range(len(possibleWins)):
        
            # Checking for a continuous run with no instances of possibleWins[i][i2]!=player
            Blocked=False
            for i2 in range(len(possibleWins[i])):

                if board[possibleWins[i][i2]]!=player:
                    Blocked=True

            # Setting won to true if the current run is continuous, with no instances of possibleWins[i][i2]!=player
            if Blocked==False:
                Won=True
        return Won

    def game_over(self):
        # VARIABLES
        global board
        over=False
        full=True

        # Checking if board is NOT full
        for i in range(len(board)):
            if board[i]=='*':
                full=False
        
        # Setting over=true if the board is full or either player has won
        if full==True or TTTBoard.has_won(TTTBoard,"X")==True or TTTBoard.has_won(TTTBoard,"O")==True:
            over=True
        return over
    
    def clear(self):
        global board
        board=["*","*","*","*","*","*","*","*","*"]
    



    pass

def play_tic_tac_toe() -> None:
    """Uses your class to play TicTacToe"""

    def is_int(maybe_int: str):
        """Returns True if val is int, False otherwise

        Args:
            maybe_int - string to check if it's an int

        Returns:
            True if maybe_int is an int, False otherwise
        """
        try:
            int(maybe_int)
            return True
        except ValueError:
            return False

    brd = TTTBoard()
    players = ["X", "O"]
    turn = 0

    while not brd.game_over():
        print(brd)
        move: str = input(f"Player {players[turn]} what is your move? ")

        if not is_int(move):
            raise ValueError(
                f"Given invalid position {move}, position must be integer between 0 and 8 inclusive"
            )

        if brd.make_move(players[turn], int(move)):
            turn = not turn

    print(f"\nGame over!\n\n{brd}")
    if brd.has_won(players[0]):
        print(f"{players[0]} wins!")
    elif brd.has_won(players[1]):
        print(f"{players[1]} wins!")
    else:
        print(f"Board full, cat's game!")


if __name__ == "__main__":
    # here are some tests. These are not at all exhaustive tests. You will DEFINITELY
    # need to write some more tests to make sure that your TTTBoard class is behaving
    # properly.

    
    brd = TTTBoard()
    brd.make_move("X", 8)
    brd.make_move("O", 7)

    assert brd.game_over() == False

    brd.make_move("X", 5)
    brd.make_move("O", 6)
    brd.make_move("X", 2)

    assert brd.has_won("X") == True
    assert brd.has_won("O") == False
    assert brd.game_over() == True

    brd.clear()

    assert brd.game_over() == False

    brd.make_move("O", 3)
    brd.make_move("O", 4)
    brd.make_move("O", 5)

    assert brd.has_won("X") == False
    assert brd.has_won("O") == True
    assert brd.game_over() == True
    

    print("All tests passed!")

    # uncomment to play!
    play_tic_tac_toe()
