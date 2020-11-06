import random

number = random.randrange(1,50)
guess = int(input("Guess between 1 and 50\n"))

while guess != number :

    if  guess < number:
        print("Guess higher, Try again")
        guess = int(input("\nGuess a number again 1 50\n"))
    else:
        print("Guess lower try agane")
        guess = int(input("\nGuess a number again 1 50\n"))

print("You guessed correctly")