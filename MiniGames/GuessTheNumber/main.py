import random

def game():
    number_of_guess = 10

    number = random.randrange(100)
    while number_of_guess > 0:
        user_input = int(input("Enter the number : "))

        if user_input == number:
            print("You win...")
            play_again()
        elif user_input > number:
            print("Too high...")
        elif user_input < number:
            print("Too low...")

        number_of_guess -= 1
        print("Guess remaining",number_of_guess)

        if number_of_guess == 0:
            print("Game over")
            print("Number was",number)
            play_again()

def play_again():
    user_ch = input("Do you want to play again ? ")
    if user_ch.lower() == 'yes':
        game()
    else:
        quit()

game()