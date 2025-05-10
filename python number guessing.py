import random

low_num = 1
hi_num = 100
answer = random.randint(low_num, hi_num)
count = 0
is_running = True

print("""     !!!!!!!Welcome!!!!!!! """)
print(""" To the number guessing game""")
print(""" Pro tip: Start with 50 to make it easy\n""")
print(f"Select a number between {low_num} and {hi_num}\n")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        count += 1

        if guess < low_num or guess > hi_num:
            print("That number is not within the given range")
            print(f"Select a number between {low_num} and {hi_num}\n")
        elif guess > answer:
            print("Too high! Please try again.\n")
        elif guess < answer:
            print("Too low! Please try again.\n")
        else:
            print(f"\nCORRECT!!!!! The answer is {answer}")
            print(f"Number of guesses: {count}")
            is_running = False
    else:
        print(f"Enter a valid number between {low_num} and {hi_num}")
