from random import randint

#creat a list of play options
t = ["Rock", "Paper", "Scissors"]

#assign random play to the computer
computer = t[randint(0, 2)]

#intialize the player with the false value
player = False
while player == False:
    player = input("Rock, Paper, Scissors? : ")
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose", computer, "smashes", player )
        else:
            print("You win!", player, "cut", computer)
    else:
        print("That's invalid play. Check your spelling!")

    player = False
    computer = t[randint(0, 2)]



