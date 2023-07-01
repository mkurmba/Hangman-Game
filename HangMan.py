import time
import random

print("\nWelcome to Hangman!\n")
name = input("Enter your name: ")
print("Hi " + name + "! Best of Luck!!")
time.sleep(2)
print("The game is starting now!\nLet's play Hangman!!")
time.sleep(3)

def main():
    global count
    global display
    global word
    global guessedLetters
    global length
    global playGame
    global hangManlvls

    word = random.choice(guessWords)
    length = len(word)
    count = 0
    display = '_' * length
    guessedLetters = []
    playGame = ""

    hangManlvls = ['''
    +---+
        |
        |
        |
        |
      =====''','''
    +---+
    |   |
        |
        |
        |
      =====''','''
    +---+
    |   |
    O   |
    |   |
        |
      =====''','''
    +---+
    |   |
    O   |
  / |   |
        |
      =====''','''
  +---+
    |   |
    O   |
  / | \ |
        |
      =====''','''
    +---+
    |   |
    O   |
  / | \ |
   /    |
      =====''','''
    +---+
    |   |
    O   |
  / | \ |
   / \  |
      =====''']


guessWords = ['checks']

def guessOcurrence(guess):
    chrCnt = 0
    letters = []
    for i in word:
        if i == guess:
            chrCnt += 1
            letters.append(i)
    return chrCnt, letters
def playLoop():
    global playGame
    playGame = input("Run it back? y = yes, n = no \n")
    while playGame not in ["y", "n", "Y", "N"]:
        playGame = input("Do You want to play again? y = yes, n = no \n")
    if playGame == "y":
        main()
    elif playGame == "n":
        print("Thanks For Playing!!")
        exit()

def hangMan():
    global count
    global display
    global word
    global guessedLetters
    global playGame
    global hangManlvls
    finalWord = word
    limit = 7
    guess = input("The Hangman Word is: " + display + " Enter your guess: \n")
    guess = guess.strip()
    if not guess.isalpha() or len(guess) == 0 or len(guess) >= 2:
        print("Invalid Input, Try a letter\n")
        hangMan()

    elif guess in word:

        guessedLetters.extend([guess])
        occur, letters = guessOcurrence(guess)
        for i in range(occur):

            letterIdx = word.find(letters[i])
            word = word[:letterIdx] + "_" + word[letterIdx + 1:]
            display = display[:letterIdx] + guess + display[letterIdx + 1:]
        print("Secret Word: "+ display + "\n")

    elif guess in guessedLetters:
        print("Guess repeated, Try another letter.\n")

    else:
        count += 1
        if count == 1:
            time.sleep(1)
            print(hangManlvls[0])
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print(hangManlvls[1])
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print(hangManlvls[2])
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print(hangManlvls[3])
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 5:
            time.sleep(1)
            print(hangManlvls[4])
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 6:
            time.sleep(1)
            print(hangManlvls[5])
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")
        elif count == 7:
            time.sleep(1)
            print(hangManlvls[6])
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", guessedLetters, finalWord)
            playLoop()


    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        playLoop()
    elif count != limit:
        hangMan()


main()
hangMan()
