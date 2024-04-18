# create game of rock paper scissors
# user input
# computer random choice
# compare choices
# display results

import random

print("Welcome to Rock, Paper, Scissors!")
print("Best of 3 rounds wins!")

player_score = 0
computer_score = 0
play_again = "";

# after the game is over, the player_score and computer_score will be displayed and user should have option to play again or not
# if user decides to play again, reset player_score and computer_score and play again
# if user decides to not play again, display "Thanks for playing!"
# if user enters anything other than yes or no, display "Invalid input! Please enter yes or no."
# if user enters anything other than rock paper or scissors, display "Invalid input! Please enter rock, paper, or scissors."
while player_score < 3 and computer_score < 3 and play_again != "no":
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose {computer_choice}.")

    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print("Invalid input! Please enter rock, paper, or scissors.")
        continue
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You win! Rock beats scissors!")
        player_score += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("You win! Paper beats rock!")
        player_score += 1
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You win! Scissors beats paper!")
        player_score += 1
    else:
        print(f"Computer wins! {computer_choice} beats {user_choice}!")
        computer_score += 1

    print(f"Player: {player_score} Computer: {computer_score}")


    
    if player_score == 3 or computer_score == 3:
        print("Game over!")
        while True:
            play_again = input("Do you want to play again? (yes/no): ").lower()
            if play_again == "yes":
                player_score = 0
                computer_score = 0
                break
            elif play_again == "no":
                print("Thanks for playing!")
                break
            else:
                print("Invalid input! Please enter yes or no.")
    
            
