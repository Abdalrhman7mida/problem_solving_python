print('think of a number between 0 to 100, and we will get it right fast !')
# Set initial range of numbers
low = 0
high = 100
# Initialize state variable to control the loop
state = True

# Loop until the secrete number is found
while state:
    # Calculate the midpoint of the range
    medium = (high + low) // 2
    # Ask the user if their secret number is the midpoint
    guess = input(
        f"Is your number {medium}? Enter 'h' to indicate the guess is too high, 'l' to indicate is too low, "
        f"'c' to indicate it's correct: ").strip().lower()

    # If the guess is correct, end the game
    if guess == 'c':
        print(f'game over, your secrete number = {medium}!')
        state = False
    # If the guess is too high, adjust the range accordingly
    elif guess == 'h':
        high = medium
    # If the guess is too low, adjust the range accordingly
    elif guess == 'l':
        low = medium
    # If user enters an invalid input, ask again
    else:
        print("invalid input, please enter 'h', 'l', 'c'.")
