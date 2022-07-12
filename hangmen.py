from time import sleep
from os import system
from random import choice

system('clear')
print("Welcome to the Hangmen Game!")
sleep(2)
print("Gusess the word to win the game!")
sleep(2)
name = input("\nEnter your name: ")
print("\nWelcome", name.strip() + "! Let's get started")
sleep(2)
print("Good Luck!")
system('clear')


def main():
    global dashs
    global word
    global length
    global guess
    global already_guessed
    global wordToGuess
    global wordChosen
    global limit
    global playGame

    limit = 0
    wordsToGuess = [
        "january",
        "border",
        "image",
        "film",
        "promise",
        "kids",
        "lungs",
        "doll",
        "rhyme",
        "damage",
        "plants",
    ]
    already_guessed = []
    word = choice(wordsToGuess)
    wordToGuess = list(word)
    length = len(word)
    wordChosen = list(word)
    playGame = 'y'
    dashs = ["_" for x in range(length)]


def hangmen():
    global limit
    # print("word", wordToGuess)
    print("\nThe Word is ", *dashs, sep='')
    guess = input("\nEnter your guess: ")
    guess = guess.strip()

    if len(guess) == 0 or len(guess) >= 2:
        system("clear")
        print("Invalid input! Try a Letter \n")

    elif guess in wordToGuess:
        system("clear")
        already_guessed.append(guess)
        index = wordToGuess.index(guess)
        wordToGuess[index] = "_"
        dashs[index] = guess

    elif guess in already_guessed:
        system("clear")
        print("Already Gussed! Try another letter.\n")

    else:
        limit += 1

        if limit == 1:
            system("clear")
            print("Wrong Answer", 5 - limit, "chance left\n")
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif limit == 2:
            system("clear")
            print("Wrong Answer", 5 - limit, "chance left\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif limit == 3:
            system("clear")
            print("Wrong Answer", 5 - limit, "chance left\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif limit == 4:
            system("clear")
            print("Wrong Answer Last chance left\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")

        elif limit == 5:
            system("clear")
            print("Wrong Answers You are hanged!!!\n")
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")

    if dashs == wordChosen:
        playGameLoop = True
        print("Congrats! You have guessed the word correctly!")
        print("The word was", word)
        while playGameLoop:
            playGame = input("Do you want to play again? ")
            if playGame == 'y' or playGame == 'Y':
                system('clear')
                main()
                hangmen()
                playGameLoop = False
            elif playGame == 'n' or playGame == 'N':
                system("clear")
                print("Thank you for Playing Game!")
                playGameLoop = False
            else:
                system("clear")
                print("Wrong Choice Enter again!\n")
                playGameLoop = True

    elif limit == 5:
        print("Game Over!!!")
        print("The correct word was", word)

    else:
        hangmen()


main()
hangmen()
