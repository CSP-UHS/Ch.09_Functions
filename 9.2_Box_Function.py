'''
BOX_FUNCTION
------------
Write a function called box that will output boxes (made of lower case o's) 
given a height and width. Once you've finished writing your function, copy 
and paste the following code after it and make sure it works with the function you wrote:

INPUT
-----
box(7,5) # Print a box 7 high, 5 across
print() # Blank line
box(3,2) # Print a box 3 high, 2 across
print() # Blank line
box(3,10) # Print a box 3 high, 10 across

OUTPUT
------
ooooo
ooooo
ooooo
ooooo
ooooo
ooooo
ooooo

oo
oo
oo

oooooooooo
oooooooooo
oooooooooo
'''


def program():
    global running
    running = True

    def cbox():
        global running
        while running:
            base = int(input("Base: "))
            height = int(input("Height: "))
            print()
            for i in range(height):
                print("o" * base + "\r")
            print()
            print("Run again?")
            print("[Y] [N]")
            print()
            choice = input("Input: ")
            print()
            if choice.lower() == "n":
                running = False

    def box(height, base):
        for i in range(height):
            print("o" * base + "\r")

    while True:
        print("Would you like to run a custom box, or a preset grouping of boxes?")
        print("[C] [P]")
        print()
        choice = input("Input: ")
        print()
        if choice.lower() == "c":
            cbox()
        elif choice.lower() == "p":
            box(7, 5)
            print()
            box(3, 2)
            print()
            box(3, 10)
            print()
            print("Run again?")
            print("[Y] [N]")
            print()
            choice = input("Input: ")
            print()
            if choice.lower() == "n":
                running = False


if __name__ == "__main__":
    program()
