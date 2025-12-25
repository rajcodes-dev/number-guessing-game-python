import random
# Number Guessing Game 
print("-----Welcome to 'Guess the number' game.-----")

run = True
# A loop to run game, Until the correct guess.
while(run):
    # random number generator between 1 to 100.
    rand_no = random.randint(1,100)
    # A counter variable which use to store number of guesses.
    attempt = 0
    while(True):
        user_guess = input("Guess the number: ")
        user_guess = user_guess.strip()

        if user_guess.isdigit() and 1 <= int(user_guess) <= 100:
            attempt = attempt + 1
            user_guess = int(user_guess)
            if rand_no == user_guess:
                print("Hooray! You guess the correct number.")
                break

            elif attempt > 10:
                print("Game Over!!!")
                print("The number was ",rand_no)
                break

            elif rand_no > user_guess:
                print("Too low!, Guess high\n")

            elif rand_no < user_guess:
                print("Too high!, Guess low\n")

        else:
            print("Guess the correct whole number b/w 1 and 100.\n")

    print("You Guess the number in ",attempt ," attempts.\n")
    # Add a conditon if you want play or not 
    play = input("Do you want to play again? (y/n)\n")
    if 'n' == play.lower():
        run = False