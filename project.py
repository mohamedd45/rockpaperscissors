from random import randint

choices = ["rock", "paper", "scissors"]
player_score = 0

while True:
    computer = choices[randint(0, 2)]
    player = input("rock, paper, or scissors? (or exit) ")

    if player == "exit":
        print("The game has now ended")
        break
    elif player in choices:
        if player == computer:
            print("Tie!")
        elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
            player_score += 1
            print("You win!", player, "beats", computer)
        else:
            print("You lose!", computer, "beats", player)
    else:
        print("Invalid input! Please choose rock, paper, or scissors.")

print("Your final score:", player_score)