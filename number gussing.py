import random

target = random.randint(1, 10)

print("I have selected a number between 1 and 10. Can you guess it?")

while True:
  
    guess = int(input("Enter your guess: "))

    if guess == target:
        print("Congratulations! You guessed it right.")
        break
    elif guess < target:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
