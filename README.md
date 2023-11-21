# rock-paper-scissors-game
<div align='center'>

<h1>Rock-Paper-Scissor Game USING PYTHON</h1>
<p>This code implements a Rock-Paper-Scissor Game USING PYTHON .
  Here's a  working pattern of this code:
  Certainly! Let's break down the working pattern of your code into five key lines:

Randomly Choose Computer's Move:


computer_choice = random.choice(list_value)
This line randomly selects the computer's move (rock, paper, or scissors) from the list of possible values.
User Input and Game Logic:


user_choice = input("[rock, paper, scissors]\nchoose any one of the following to play the game: ").lower()
This line prompts the user to input their choice and converts it to lowercase for case-insensitive comparison. It captures the user's move.
Compare User and Computer Moves:


if user_choice in ['rock', 'paper', 'scissors']:
    # ... (game logic comparing user_choice and computer_choice)
else:
    print("Enter a valid input ")
    rock_paper_scissors()
This section checks if the user's input is valid. If valid, it compares the user's choice with the computer's choice and determines the winner based on the rules of Rock, Paper, Scissors. If the user's input is invalid, it prompts the user to enter a valid input and restarts the game.
Ask User to Continue:


continue_game()
After determining the game outcome, this line calls the continue_game() function. This function asks the user if they want to continue playing. If the answer is "yes," the game restarts; if "no," the program exits.
Start or Exit the Game:


getting_input_to_start = input("Do you want to play the game[yes\\no] :")
This line asks the user whether they want to start the game or exit. If the user chooses to play, it calls the rock_paper_scissors() function to begin the game. If the user chooses to exit, the program ends. If the input is invalid, it prompts the user to enter a valid input.</p>


</div>



## :star2: About the Project

## :handshake: Contact

MYDEENRAAHINA - - mydeenraahina862@gmail.com

Project Link: [https://github.com/mydeenraahina/rock-paper-scissors-game]
