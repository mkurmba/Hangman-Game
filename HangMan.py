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
    global answer
    global Category
    global foods, countries, animals, instruments, colors, sports

    foods = ['apple', 'banana', 'carrot', 'dates', 'eggplant', 'fig', 'grape', 'honeydew', 'iceberg', 'jackfruit',
             'kiwi', 'lemon', 'mango', 'nectarine', 'olive', 'papaya', 'quince', 'raspberry', 'strawberry', 'tomato',
             'ugli', 'watermelon', 'yam', 'zucchini', 'almond', 'blueberry', 'cashew', 'doughnut', 'elderberry',
             'flounder','ginger', 'hazelnut', 'iceberg', 'jicama', 'kale', 'lobster', 'mushroom', 'nutmeg', 'orange', 'pepper',
             'quinoa','rhubarb', 'squash', 'tangerine', 'unagi', 'vanilla', 'walnut', 'xigua', 'yucca', 'ziti', 'avocado',
             'barley','cabbage', 'dill', 'endive', 'fennel', 'grapefruit', 'haddock', 'jalapeno', 'kumquat', 'lime', 'milk',
             'napa','okra', 'parsley', 'quail', 'radish', 'soybean', 'turnip', 'urad', 'violet', 'wasabi', 'ximenia', 'yogurt',
             'zest','anchovy', 'beet', 'celery', 'dill', 'egg', 'feta', 'grits', 'honey', 'italian', 'jelly', 'ketchup',
             'leek', 'miso','nacho', 'onion', 'pickle', 'quail', 'rice', 'sage', 'thyme', 'udon', 'vanilla', 'waffle', 'xavier', 'yam',
             'ziti']

    countries = ['Albania', 'Andorra', 'Angola', 'Antigua', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Bahamas',
                 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia',
                 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina', 'Burundi', 'Cambodia', 'Cameroon', 'Canada',
                 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Croatia', 'Cuba', 'Cyprus', 'Denmark',
                 'Djibouti', 'Dominica', 'Ecuador', 'Egypt', 'Eritrea', 'Estonia', 'Fiji', 'Finland',
                 'France', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea',
                 'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland',
                 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait',
                 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg',
                 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall', 'Mauritania', 'Mauritius',
                 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique',
                 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Nicaragua', 'Niger', 'Nigeria', 'Norway', 'Oman',
                 'Pakistan','Palau', 'Panama', 'Paraguay', 'Peru', 'Poland', 'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda',
                 'Samoa', 'Senegal', 'Serbia', 'Seychelles', 'Sierra', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon',
                 'Somalia', 'Spain', 'Sudan', 'Suriname', 'Sweden', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania',
                 'Thailand', 'Togo', 'Tonga', 'Trinidad', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'Uganda', 'Ukraine',
                 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe']

    animals = ['ant', 'bat', 'bee', 'cat', 'cow', 'dog', 'eel', 'elk', 'emu', 'fly', 'fox', 'gazelle', 'gnu', 'hen',
               'hog','jaguar', 'jay', 'kangaroo', 'koala', 'lion', 'lynx', 'moose', 'newt', 'orca', 'otter', 'owl', 'ox',
               'puma', 'quail', 'ram', 'rat', 'seal', 'shark', 'sheep', 'slug', 'snake', 'swan', 'tiger', 'toad', 'viper',
               'wolf','yak', 'zebra', 'ape', 'badger', 'bear', 'boar', 'bison', 'camel', 'crab', 'crow', 'deer', 'dove',
               'duck','eagle', 'falcon', 'finch', 'giraffe', 'goat', 'goose', 'hawk', 'hippo', 'ibex', 'ibis', 'jackal',
               'kiwi','lark', 'lemur', 'llama', 'loon', 'mole', 'moth', 'nymph', 'orca', 'orca', 'panda', 'parrot', 'quokka',
               'quoll','raven', 'rook', 'sloth', 'snail', 'sparrow', 'stoat', 'stork', 'swan', 'toucan', 'vole', 'wasp',
               'weasel','wren', 'yabby', 'yak', 'zebra']

    colors = ['black', 'blue', 'brown', 'cyan', 'gold', 'gray', 'green', 'indigo', 'ivory', 'lavender', 'magenta',
              'maroon','navy', 'olive', 'orange', 'pink', 'purple', 'red', 'silver', 'teal', 'violet', 'white', 'yellow',
              'aquamarine','beige', 'coral', 'crimson', 'emerald', 'fuchsia', 'khaki', 'lemon', 'lilac', 'lime', 'mauve', 'peach',
              'peridot','plum', 'raspberry', 'rose', 'ruby', 'sapphire', 'scarlet', 'tangerine', 'turquoise', 'amethyst',
              'chartreuse', 'ebony', 'garnet', 'hazel', 'jade']

    instruments = ['guitar', 'piano', 'violin', 'drums', 'flute', 'trumpet', 'saxophone', 'clarinet',
                   'cello', 'ukulele', 'harmonica', 'accordion', 'trombone', 'banjo', 'harp', 'bassoon', 'xylophone',
                   'oboe', 'mandolin', 'bagpipes', 'sitar', 'djembe', 'conga', 'didgeridoo', 'tambourine', 'marimba',
                   'keyboard', 'synthesizer', 'cymbals', 'viola', 'piccolo', 'tabla', 'kazoo', 'vibraphone',
                   'glockenspiel', 'guzheng', 'saz', 'shamisen', 'kalimba', 'charango', 'dulcimer', 'fiddle']

    sports = ['football', 'basketball', 'baseball', 'soccer', 'tennis', 'volleyball', 'golf', 'cricket', 'rugby',
              'hockey', 'badminton', 'swimming', 'athletics', 'boxing', 'cycling', 'tabletennis', 'wrestling', 'gymnastics',
              'skiing', 'snowboarding', 'surfing', 'sailing', 'rowing', 'karate', 'judo', 'taekwondo', 'archery',
              'shooting', 'fencing', 'canoeing', 'kayaking', 'triathlon', 'trampoline', 'weightlifting', 'handball',
              'icehockey', 'figureskating', 'bobsleigh', 'luge', 'curling', 'snooker', 'darts', 'cricket', 'polo',
              'racing', 'netball', 'waterpolo', 'lacrosse', 'squash', 'rollerskating', 'skateboarding',
              'parkour', 'rockclimbing', 'mountaineering', 'caving', 'kiteboarding', 'paragliding', 'powerlifting',
              'breakdancing', 'handball', 'muaythai', 'motorsport', 'equestrian',
              'paddleboarding', 'yoga', 'crossfit', 'aerobics', 'ballet', 'cheerleading']

    categories = [foods, countries, colors, instruments,sports, animals]
    Category = random.choice(categories)
    word = random.choice(Category)
    word = word.lower()
    answer = word
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
    global answer
    global Category
    global foods , countries, animals, instruments, colors, sports
    limit = 7

    if Category == foods:
        print("Hint: Food")
    elif Category == countries:
        print("Hint: Country")
    elif Category == animals:
        print("Hint: Animals")
    elif Category == instruments:
        print("Hint: Musical Instruments")
    elif Category == colors:
        print("Hint: Colors")
    elif Category == sports:
        print("Hint: Sports")
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
            print("The word was:",answer)
            playLoop()


    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        playLoop()
    elif count != limit:
        hangMan()


main()
hangMan()



