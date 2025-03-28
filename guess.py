import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guessess = 0
is_running = True

print("Python Guessing Game")
print(f"Guess a number between {lowest_num} and {highest_num}.")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guessess += 1

        if guess < lowest_num or guess > highest_num:
            print("Please enter a number between 1 and 100.")
        elif guess < answer:
            print("Too low. Try again.")
        elif guess > answer:
            print("Too high. Try again.")
        else:
            print(f"You guessed it in {guessess} guesses!")
            is_running = False
    else:
        print("Please enter a number.")
        print("Please select a number between {lowest_num} and {highest_num}.")