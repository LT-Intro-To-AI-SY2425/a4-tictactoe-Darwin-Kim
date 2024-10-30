# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?

For me, the most difficult part was figuring out how to tell if the game has been won or not. initially, I attempted to start at a certain position and then probe the board values that correalated to positions that were diagonal, straight across, straight down or straight up from that position. This strategy would be better if the board was bigger. However, I soon discovered that since the board was so small, it would be faster to simply make a list of possible win "scenarios" and check if the current board state matched one of those scenarios.

2. Explain how you would add a computer player to the game.

I would make another object which would interface with the game by manipulating the global variable "board". This would be beneficial for organizational purposes, since it would allow me to have a separate set of functions inside that object that would be explicitely different from the main functions to create the board, as well as functional purposes, since it would allow me to call each object seperately as needed, therefore reducing the number of functions that the computer has to search through to find the correct function, increasing speed and reducing the risk of errors from both the human and the computer.

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.

First off, I would have the computer always start in the middle. This is normally the best move. Then, I would have variables for each empty square that would give the computer information on that square, such as the distance from that square to the nearest square that it has filled, as well as wether that square is between two squares occupied by the opponent. 