"""
A number guessing game
"""
import random


def guess_num(low_num, high_num, cpu_num, total_guesses):
    guess_range = [low_num, high_num]
    print(f"CPU has picked a number between {low_num} and {high_num}")
    # Initial first guess and addition to the total number of guesses
    user_guess = int(input(f"Please guess my number: "))
    total_guesses += 1
    if user_guess in range(int(guess_range[0]), int(guess_range[1])):
        # Keep looping until the user guesses the number
        while user_guess != cpu_num:
            if user_guess < cpu_num:
                print(f"Try again! You guessed too small.\n")
                guess_range[0] = user_guess
            elif user_guess > cpu_num:
                print(f"Try again! You guessed too high.\n")
                guess_range[1] = user_guess
            print(f"The range is now between {guess_range[0]} and {guess_range[1]}")
            user_guess = int(input(f"Please guess my number: "))
            total_guesses += 1
        print(f"\nThat is correct! My number was {cpu_num}. You got it in {total_guesses} guesse(s).")
    else:
        print(f"Value entered is outside of valid range [{guess_range[0]}-{guess_range[1]}]")
        return None
    return None


def pick_cpu_num(low_num, high_num):
    # Function to randomly select a number within the range the user gives and return it.
    cpu_num = random.randrange(low_num, high_num)
    return cpu_num


def main():
    total_guesses = 0
    try:
        user_range_low = int(input("Please enter the lowest possible number in range:- "))
        user_range_high = int(input("Please enter the higest possible number in range:- "))
        if user_range_low == 0 or user_range_high == 0:
            print("Please do not use 0")
            return None
        # Picks a random number in range
        cpu_num = pick_cpu_num(user_range_low, user_range_high)
        # Starts the guessing game function
        guess_num(user_range_low, user_range_high, cpu_num, total_guesses)
    except ValueError:
        print(f"Please use integer numbers such as 1, 2, 100... etc") 


if __name__ == "__main__":
    main()