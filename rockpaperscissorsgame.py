import random
def play_game():
    def rock_paper_scissors():
        def continue_game():
            while True:
                input_to_continue=input(f"do you continue this game [yes\\ no]:")
                if input_to_continue.lower()=="yes":
                    rock_paper_scissors()
                elif input_to_continue.lower()=="no":
                    print(f"Exit!")
                    break
                else:
                    print(f"Enter a  valid input ")
                    rock_paper_scissors()
        user_choice=input("[rock,paper,scissors]\nchoose any one of the following to play the game :").lower()
        if user_choice in['rock','paper','scissors']:
            print(f"{user_choice=}")
            print(f"{computer_choice=}")
            if (user_choice=="rock" and computer_choice=="scissors" or
                user_choice == "paper" and computer_choice=="rock" or
                user_choice == "scissors" and computer_choice=="paper"):
                    print("user won the game")
            elif user_choice==computer_choice:
                print(f"Game Tied")
            else:
                print(f"computer won the game")
        else:
            print(f"Enter a  valid input ")
            rock_paper_scissors()
        continue_game()
    print(f"rock,paper,scissors game")
    list_value=["rock","paper","scissors"]
    computer_choice=random.choice(list_value)
    while True:
        getting_input_to_start=input(f"Do you want to play the game[yes\\no] :")
        if  getting_input_to_start.lower()=="yes":
            rock_paper_scissors()
        elif  getting_input_to_start.lower()=="no":
            print(f"Exit!")
            break
        else:
            print(f"Enter a  valid input ")
play_game()
