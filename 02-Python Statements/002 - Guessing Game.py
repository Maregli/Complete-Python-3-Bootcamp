# Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
#
# If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
# On a player's first turn, if their guess is
# within 10 of the number, return "WARM!"
# further than 10 away from the number, return "COLD!"
# On all subsequent turns, if a guess is
# closer to the number than the previous guess return "WARMER!"
# farther from the number than the previous guess, return "COLDER!"
# When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!

from random import randint

guess  = int(input("Insert your number here: "))
x = randint(0,100)
guesslis = []
print(x)

while guess != x:
    if guess not in range(0,101):
        print("out of bounds")
        guesslis.append(guess)
        guess = int(input("Insert new guess: "))
    elif len(guesslis) == 0:
        if abs(guess - x) <= 10:
            print("Warm!")
        else:
            print("Cold!")
        guesslis.append(guess)
        guess = int(input("Insert new guess: "))
    else:
        if abs(guesslis[-1]-x) > abs(guess-x):
            print("Warmer")
        else:
            print("Colder")
        guesslis.append(guess)
        guess = int(input("Insert new guess: "))
print("Congratulations, you guessed the number")
print(f'Your number of attempts: {len(guesslis)}')


