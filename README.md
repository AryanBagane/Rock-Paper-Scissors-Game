# Rock-Paper-Scissors-Game
Rock-Paper-Scissors Game
This Python script implements a simple console-based Rock-Paper-Scissors game. Players can input their choice (rock, paper, or scissors), and the computer will randomly select its choice. The game then determines the winner based on the classic Rock-Paper-Scissors rules.

Code Description
1. get_choice function
This function takes user input for their choice (rock, paper, or scissors).
It generates a random choice for the computer using the random.choice function.
The player and computer choices are stored in a dictionary and returned.
2. check_win function
This function compares the player and computer choices to determine the winner.
It utilizes nested if-else conditions to cover all possible scenarios.
The result is returned as a string indicating whether it's a tie or which player won.
3. Running the Game
The user's choices are obtained by calling the get_choice function.
The check_win function is then called with the player and computer choices.
The result is printed to the console, indicating the winner or a tie.

Code Features
Use of functions to organize and modularize the code.
Utilization of lists, dictionaries, and the random module.
Implementation of nested if-else conditions for decision-making.
Use of formatted strings (f-strings) for concise output.

How to Play
Run the script.
Enter your choice when prompted (rock, paper, or scissors).
The computer will randomly select its choice.
The winner or a tie will be displayed.
Enjoy playing Rock-Paper-Scissors!
