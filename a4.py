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

        # Attempting to run checks on board[pos], then returning false if calling board[pos] results in an index error
        try:
            # Checking if the position on the board is set to "*", then making the move if both conditions are true
            if board[pos]=="*": 
                board[pos]=player

            # Returning True if move was made, otherwise returning False
            return True if board[pos]==player else False
        
        # Attempting to run checks on board[pos], then returning false if calling board[pos] results in an index error
        except IndexError:
            return False
        
        # ORIGINAL METHOD:
        #if board[pos]=="*" and pos<len(board):
        #     board[pos]==player
        #return True if pos<len(board) and board[pos]==player else False
            
    def has_won(self, player):
        # VARIABLES
        Won=False

        # Checking if current board index (i) and board indexes i2 spaces away from it are all valid (less than len(board)) and
        # equal to player, then setting Won to true if both conditions are met
        for i in range(len(board)):
            for i2 in range(1,5,1):
                if 0<i-i2<len(board) and 0<i+i2<len(board) and board[i-i2]==board[i]==board[i+i2]==player:
                    Won=True
        return Won
    
        #ORIGINAL METHOD:
        # PossibleWins=[(list of possible wins here, forgot what it was and didn't want to type it again, but it's in the format of [scenario 1[position 1, position 2, position 3,]],[scenario 2[position 1, position 2, position 3,]], etc)]
        # Won=False
        # for i in range(PossibleWins):
        #    Win=True
        #    for i2 in range(PossibleWins[i])
        #        if player!=board[PossibleWins[i][i2]]:
        #             Win=False
        #    if Win=True:
        #       Won=True
        # return Won
                    




    def game_over(self):
               
        # Returning True if the board is full or either player has won or if there are no astericks within the board, else returning False
        if "*" not in board or self.has_won("X") or self.has_won("O"):
            return True
        else:
            return False
        
        # Original method mostly the same, but if conditions are less optomized and more wordy
    
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