#Sign your name:________________


#1.) Correct the following code: (The user's number should be increased by 1 and printed.)


def increase(x):
    return x + 1

num = int(input("Enter a number: "))
num2 = increase(num)
print("Your number has been increased to", num2)

#2.) Correct the following code to print 1-10:


def count_to_ten():
    for i in range(1, 11):
        print(i)

count_to_ten()

#3.) Correct the following code to sum the list:


def sum_list(list):
    sum = 0
    for item in list:
        sum += item
    return sum

list = [45, 2, 10, -5, 100]
print(sum_list(list))

#4.) Correct the following code which should reverse the sentence that is entered.


def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[i - 1]
    return result

text = str(input("Enter a sentence: "))
print(reverse(text))

#5.) Correct the following code: (if one of the options is not entered it should print the statements)


def get_user_choice():
    while True:
        command = input("Command: ")
        if command.lower() == "f":
            out = "f - Full speed ahead"
        elif command.lower() == "m":
            out = "m - Moderate speed"
        elif command.lower() == "s":
            out = "s - Status"
        elif command.lower() == "d":
            out = "d - Drink"
        elif command.lower() == "q":
            out = "q - Quit"
        else:
            out = "Hey, that's not a command. Here are your options:"
        return out

user_command = get_user_choice()
print("You entered:", user_command)

