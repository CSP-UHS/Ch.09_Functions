# #Sign your name: Samuel Pattison
#
#
# #1.) Correct the following code: (The user's number should be increased by 1 and printed.)
#
# def increase(x):
#     num = x + 1
#     return num
#
#
# num = int(input("Enter a number: "))
# increase(num)
# x = increase(num)
# print("Your number has been increased to", x)
#
#

#
# #2.) Correct the following code to print 1-10:
#
# def count_to_ten():
#     for i in range(1,11):
#         print(i)
#
# count_to_ten()
#
#

#3.) Correct the following code to sum the list:
#
# def sum_list(list):
#     sum = 0
#     for i in list:
#         sum += i
#     return sum
# list = [45,2,10,-5,100]
# sum = sum_list(list)
# print(sum)
#
#

#
# #4.) Correct the following code which should reverse the sentence that is entered.
#
# def reverse(text):
#     result = ""
#     text_length = len(text)
#     for i in range(text_length):
#         result = result + text[(i + 1) * -1]
#     return result
#
# text = input("Enter a sentence: ")
# print(reverse(text))
#


#5.) Correct the following code: (if one of the options is not entered it should print the statements)

def get_user_choice():
    while True:
        command = input("Command: ")
        if command == "f":
            print("f - Full speed ahead")
            return command
        elif command == "m":
            print("m - Moderate speed")
            return command
        elif command == "s":
            print("s - Status")
            return command
        elif command == "d":
            print("d - Drink")
            return command
        elif command == "q":
            print("q - Quit")
            return command
        else:
            print("Hey, that's not a command. Here are your options:" )
            return command






user_command = get_user_choice()
print("You entered:", user_command)

