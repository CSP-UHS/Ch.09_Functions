def hangman():
    print("    ------")
    print("   |      |")
    print("   |")
    print("   |")
    print("   |")
    print("   |")
    print("_______")
    print("")
    print("Word is:", letters)
lose = 0

letters = ""
guessed = "Wrong guesses: "

choice = input("What would you like your word to be?")
print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")

length = len(choice)
for i in range(length):
    letters += "_"

lol = length-1

done = False
while not done:
    if lose == 0:
        hangman()
    win = -1
    if lose == 1:
        def hangman():
            print("    ------")
            print("   |      |")
            print("   |      O")
            print("   |")
            print("   |")
            print("   |")
            print("_______")
            print("")
            print("Word is:", letters)

    if lose == 2:
        def hangman():
            print("    ------")
            print("   |      |")
            print("   |      O")
            print("   |      |")
            print("   |")
            print("   |")
            print("_______")
            print("")
            print("Word is:", letters)

    if lose == 3:
        def hangman():
            print("    ------")
            print("   |      |")
            print("   |      O")
            print("   |     \|")
            print("   |")
            print("   |")
            print("_______")
            print("")
            print("Word is:", letters)

    if lose == 4:
        def hangman():
            print("    ------")
            print("   |      |")
            print("   |      O")
            print("   |     \|/")
            print("   |")
            print("   |")
            print("_______")
            print("")
            print("Word is:", letters)

    if lose == 5:
        def hangman():
            print("    ------")
            print("   |      |")
            print("   |      O")
            print("   |     \|/")
            print("   |     /")
            print("   |")
            print("_______")
            print("")
            print("Word is:", letters)

    if lose == 6:
        def hangman():
            print("    ------")
            print("   |      |")
            print("   |      O")
            print("   |     \|/")
            print("   |     / \\")
            print("   |")
            print("_______")
            print("")
            print("Word is:", letters)
        print("Game over!")
        print("The word was: ", choice)
        done = True
    guess = input("What letter would you like to guess?")
    win = -1
    if guess in choice:
        for i in choice:
            win += 1
            if i == "":
                continue
            if i == guess:
                list1 = list(letters)
                list1[win]=guess
                letters=''.join(list1)
            else:
                continue

    if guess not in choice:
        lose += 1
        hangman()
        guessed += guess
        print(guessed)

    if "_" in letters:
        continue
    if "_" not in letters:
        print("You won! \nGame over")
        done = True