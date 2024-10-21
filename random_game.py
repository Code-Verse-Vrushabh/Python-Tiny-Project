from random import randint

def main():
    print("Welcome to the User-Input Random Number Guessing Game!")

    # Get user-defined range
    while True:
        try:
            lower_bound = int(input("Please enter the lower bound of the range: "))
            upper_bound = int(input("Please enter the upper bound of the range: "))
            if lower_bound >= upper_bound:
                print("Lower bound must be less than upper bound. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter valid integer values for the bounds.")

    answer = randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Guess a number between {lower_bound} and {upper_bound}.")

    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1

            if guess < lower_bound or guess > upper_bound:
                print(f"Please guess a number within the range {lower_bound} to {upper_bound}.")
                continue

            if guess == answer:
                print(f"Correct! You've guessed the number in {attempts} attempts. Genius!")
                break
            elif guess < answer:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        except ValueError:
            print("Please enter a valid number.")

    # Ask if the player wants to play again
    play_again = input("Would you like to play again? (yes/no): ").strip().lower()
    if play_again == 'yes':
        main()  # Restart the game
    else:
        print("Thank you for playing! Goodbye.")

if __name__ == "__main__":
    main()
