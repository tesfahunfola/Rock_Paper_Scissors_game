import random

number = random.randint(1, 10)

player_name = input("Hello, What's your name? ")
number_of_guesses = 0

print("Okay,", player_name,",","I am guessing a number between 1 to 10.")

print("What's your guess number from 1 to 10? ")

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1

    if guess < number:
        print("Your guess is too low!")
    elif guess > number:
        print("Your guess is too high!")
    else:
        break

if guess == number:
    print("Congratulations, ", player_name, "! You guessed the number in ", str(number_of_guesses), "tries!")
else:
    print("Sorry, ", player_name, "you didn't guess the number. The number was ", str(number))