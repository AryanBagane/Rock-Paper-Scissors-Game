import random
                      
def get_choice():
    player_choice = input("Enter a choice (rock, paper, scissiors): ")
    options = ['rock', 'paper', 'scissiors']
    computer_choice = random.choice(options) # Use of random function
    choices = {
        "player": player_choice, "computer": computer_choice
    }

    return choices

def check_win(player, computer):
    print(f"You chose {player}, Computer chose {computer}") # concatenation using f-string

    # Use of nested IF-ELSE Condition
    if player == computer:
        return "It's a Tie."
    elif player == "rock":
        if computer == "scissors":
            return "rock smashes scissors, You won :)"
        else:
            return "paper wraps rock, You lose :("
        
    elif player == "paper":
        if computer == "scissors":
            return "scissors cuts paper, You lose :("
        else:
            return "paper wraps rock, You won :)"
        
    elif player == "scissors":
        if computer == "rock":
            return "rock smashes scissors, You lose :("
        else:
            return "scissors wraps paper, You won :)"
    
choices = get_choice()
result = check_win(choices["player"], choices["computer"])
print(result)
