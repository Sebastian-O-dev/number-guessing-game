import random

lives = 0

print("""                                                                                              
 _____ _____ _____ _____ _____     _____ _____ _____      _____ _____ _____ _____ _____ _____ 
|   __|  |  |   __|   __|   __|   |_   _|  |  |   __|    |   | |  |  |     | __  |   __| __  |
|  |  |  |  |   __|__   |__   |     | | |     |   __|    | | | |  |  | | | | __ -|   __|    -|
|_____|_____|_____|_____|_____|     |_| |__|__|_____|    |_|___|_____|_|_|_|_____|_____|__|__|
    """)
print("""
Welcome to Guess The Number game.
Your goal is to guess a random number between 1 and 100.
    """)


def diff():
    while True:
        diff_var = input("\nPick a difficulty, type \"easy\" or \"hard\": ")
        if diff_var != "easy" and diff_var != "hard":
            print("\nInvalid input")
            continue
        elif diff_var == "easy":
            lives = 10
            print(f"\nYou have {lives} lives.")
            return lives
        else:
            lives = 5
            print(f"\nYou have {lives} lives.")
            return lives


def game():
    global lives
    number_to_guess = random.randint(1, 100)
    lives = diff()
    game_cond = False
    while not game_cond:
        game_cond = check_answer(number_to_guess)
    replay = input("Do you want to play again? (y/n): ")
    if replay == "y":
        game()
    else:
        print("End of program")


def check_lives(number_to_guess):
    if lives == 0:
        print(f"\nYou have lost all your lives. The number was {number_to_guess}. Game over.")
        return True
    return False


def check_answer(number_to_guess):
    global lives
    if check_lives(number_to_guess):
        return True
    player_guess = int(input("\nYour guess: "))
    if player_guess == number_to_guess:
        print(f"\nYou win! The number was {number_to_guess}")
        return True
    if player_guess > number_to_guess:
        lives -= 1
        if check_lives(number_to_guess):
            return True
        print("\nToo high. Try again.")
        print(f"Lives left {lives}")
    else:
        lives -= 1
        if check_lives(number_to_guess):
            return True
        print("\nToo low. Try again.")
        print(f"Lives left {lives}")
    return False


game()
