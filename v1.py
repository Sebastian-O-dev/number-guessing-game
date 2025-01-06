import random
play = "yes"

while play == "yes":
    attempts_number_global = 0
    NUMBER_TO_GUESS = random.choice(range(1, 101))

    print("""                                                                                              
 _____ _____ _____ _____ _____     _____ _____ _____      _____ _____ _____ _____ _____ _____ 
|   __|  |  |   __|   __|   __|   |_   _|  |  |   __|    |   | |  |  |     | __  |   __| __  |
|  |  |  |  |   __|__   |__   |     | | |     |   __|    | | | |  |  | | | | __ -|   __|    -|
|_____|_____|_____|_____|_____|     |_| |__|__|_____|    |_|___|_____|_|_|_|_____|_____|__|__|
    """)

    print("""
Welcome to the Number Guessing Game
Your objective is to guess a number between 1 and 100.
    """)

    while True:
        difficulty = input("\nPick a difficulty \"easy\" or \"hard\": ")

        if difficulty != "easy" and difficulty != "hard":
            print("\nInvalid input, try again")
            continue
        elif difficulty == "easy":
            attempts_number_global = 10
            break
        else:
            attempts_number_global += 5
            break

    print(f"\nYou have {attempts_number_global} attempts to guess the number")

    while True:
        player_guess = int(input("\nYour guess: "))

        if player_guess == NUMBER_TO_GUESS:
            print(f"\nWell done, you have guessed the number, the number was {NUMBER_TO_GUESS}")
            break
        else:
            attempts_number_global -= 1
            if attempts_number_global == 0:
                print(f"\nGame over. No lives left, the number was {NUMBER_TO_GUESS}")
                break
            if player_guess < NUMBER_TO_GUESS:
                print(f"\nToo low. You have {attempts_number_global} attempts left. Try again.")
                continue
            else:
                print(f"\nToo high. You have {attempts_number_global} attempts left. Try again.")
                continue

    play = input(f"\nDo you want to play again? (\"yes\"/\"no\"): ")

print("End of program")
