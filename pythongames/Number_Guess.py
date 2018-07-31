import random

def game():
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            # get a number guess from player
            guess = int(input("Guess a number between 1 and 10 "))
        except ValueError:
              print("{} isn't a number!".format(guess))
        else:
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break
            elif guess > secret_num:
                print("Your number is greater than my number")
            elif guess < secret_num:
                print("Your number is less than my number")
            guesses.append(guess)
    else:
        print("You didn't get it! My number was {}".format(secret_num))
    play_again = input("Do you want to play again? Y/n ")
    if play_again.lower() != 'n':
        game()
    else:
        print("Bye!")

game()
