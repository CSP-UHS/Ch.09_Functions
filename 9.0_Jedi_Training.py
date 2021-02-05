# Sign your name: Ryan Muetzel


# 1.) Correct the following code: (The user's number should be increased by 1 and printed.)

def increase(x):
    return x + 1


num = int(input("Enter a number: "))
increase(num)
print("Your number has been increased to", increase(num))


# 2.) Correct the following code to print 1-10:

def count_to_ten():
    for i in range(10):
        print(i+1)


count_to_ten()


# 3.) Correct the following code to sum the list:

def sum_list(list):
    x = 0
    for i in range(len(list)):
        x += list[i]
    return x


list = [45, 2, 10, -5, 100]
print(sum_list(list))


# 4.) Correct the following code which should reverse the sentence that is entered.

def reverse(text):
    result = ""
    for i in range(len(text)):
        result += text[len(text) - 1 - i]
    return result


text = input("Enter a sentence: ")
print(reverse(text))


# 5.) Correct the following code: (if one of the options is not entered it should print the statements)

def get_user_choice():
    while True:
        command = input("Command: ")
        if command.upper()[:1] == 'F' or command.upper()[:1] == 'M' or command.upper()[:1] == 'S' \
                or command.upper()[:1] == 'D' or command.upper()[:1] == 'Q':
            return command
 
        print("Hey, that's not a command. Here are your options:" )
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")


print("You entered:", get_user_choice())

