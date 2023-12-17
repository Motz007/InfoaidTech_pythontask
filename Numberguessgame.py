import random

def welcome():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    print("You have 10 attempts. Let's begin!\n")

def get_player_name():
    return input("What's your name? ")

def generate_random_number():
    return random.randint(1, 100)

def play_game():
    welcome()
    player_name = get_player_name()
    play_again = True

    while play_again:
        secret_number = generate_random_number()
        attempts = 0

        while attempts < 10:
            guess = int(input("Enter your guess: "))

            if guess == secret_number:
                print(f"Congratulations, {player_name}! You guessed the correct number!")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

            attempts += 1

        if attempts == 10:
            print(f"Sorry, {player_name}. You've run out of attempts. The correct number was {secret_number}.")

        play_again = input("Do you want to play again? (yes/no): ").lower() == 'yes'

    print(f"Thanks for playing, {player_name}!")

if __name__ == "__main__":
    play_game()
