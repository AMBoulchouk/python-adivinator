import random as rd

guessesTaken = 0
minNumber = 0
maxNumber = 20

print("Hello! what is your name?: ")
username = input()

number = rd.randint(minNumber, maxNumber)

print("Well, " + username + ", I am thinking in a number between " + str(minNumber) + " and " + str(maxNumber))

##bucle del juego
while guessesTaken < 6:
    print("Take a guess: ")
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print("Your guess is too low.")
    if guess > number:
        print("Your guess is too high.")
    if guess == number:
        break

if guess == number:
    print("Good Job. " + username + "! You guessed my number in " + str(guessesTaken) + " guesses.")

if guess != number:
    print("No, the number I was thinking of was " + str(number))
