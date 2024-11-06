# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions
________________________________________________________________________________________________________________________________________

SORRY MY WRITEUP IS LONG I HAD NOTHING ELSE TO DO :(
________________________________________________________________________________________________________________________________________

1. What was the most difficult part to tic-tac-toe?
________________________________________________________________________________________________________________________________________

For me, the most difficult part was figuring out how to tell if the game has been won or not. 

initially, I attempted to start at a certain position and then probe the board values that correalated to positions that were diagonal, straight across, straight down or straight up from that position. 

This strategy was more effective, but I soon discovered a method that was less efficient but easier to implement for a smaller board. This easier method was to simply make a list of possible win "scenarios" and check if the current board state matched one of those scenarios.

Eventually though, on Friday, I had extra time and managed to figure out how to achieve the correct result using the more efficient method that was more difficult to implement. This implementation involved creating an i variable that counted from 1 to 5, then checking the current list value against the two list values i spaces away from it.
________________________________________________________________________________________________________________________________________

2. Explain how you would add a computer player to the game.
________________________________________________________________________________________________________________________________________

I would achieve this by making another object which would interface with the game by manipulating the global variable "board". 

This would be beneficial for organizational purposes, since it would allow me to have a separate set of functions inside that object that would be explicitely different from the main functions to create the board, as well as functional purposes, since it would allow me to call each object seperately as needed, therefore reducing the number of functions that the computer has to search through to find the correct function, increasing efficiency. 

A weakness of this method, however, would be the fact that it would result in more possibility for human error such as calling the wrong object. 
________________________________________________________________________________________________________________________________________

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.
________________________________________________________________________________________________________________________________________

First off, I would have the computer always start in the middle if it has the first move. This normally gives you an advantage since you have all sides open. 

Then, I would have variables for each empty square that would give the computer basic information on that square, such as the distance from that square to the nearest square that it has filled, which would be sent in as an integer, and wether that square would result in a win for either your opponent or you, both of which would be sent in as either 1 or 0, or in other words, a boolean converted into an integer. 

I would then multiply these variables by a k value that could be changed before feeding them into the computer, in order to add in the ability to adjust the strength of different responses.
________________________________________________________________________________________________________________________________________
