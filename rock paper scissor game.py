#Rock-Paper-Scissors
import random

#title of the game "Rock,Paper,Scissors"
print("Lets play Rock Paper Scissors!")

#declaring options of rock,paper,scissors
options = ("rock", "paper", "scissors")
running = True

#defining the conditions
while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter a choice ( rock, paper, scissors): ")

    print(f"player: {player}")
    print(f"computer: {computer}")
#defining the rules of the game and the winning conditions
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("you win!")
    elif player == "paper" and computer == "rock":
        print("you win!")
    elif player == "scissors" and computer == "paper":
        print("you win!")
    else:
        print("you lose!")

    play_again = input("play again? (yes/no): ").lower()
    if not play_again == "yes":
        running = False

print("Thanks for Playing!")