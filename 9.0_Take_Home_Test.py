'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Ezra McCulley



1.) Correct the following code: (The user's number should be increased by 1 and printed.)  #
'''


def increase(y):
    y += 1
    return y


x = int(input("Enter a number: "))
print("Your number has been increased to", increase(x))
print()

'''
2.) Correct the following code to print 1-10:  #
'''


def count_to_ten():
    for i in range(10):
        i += 1
        print(i)


count_to_ten()
print()

'''
3.) Correct the following code to sum the list:  #
'''


def sum_list(lis):
    x = 0
    for item in lis:
        x += item
    return x


list = [45, 2, 10, -5, 100]
print(sum_list(list))
print()



'''
4.) Correct the following code which should reverse the sentence that is entered.  # 
'''


def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[i * -1 - 1]
    return result


text = input("Enter a sentence: ")
print(reverse(text))
print()


'''
5.) Correct the following code: (if one of the options is not entered it should print the statements)  # 
'''
def get_user_choice():
    while True:
        command = input("Command: ")
        if command == "f" or command == "m" or command == "s" or command == "d" or command == "q":
            return command
 
        print("Hey, that's not a command. Here are your options:" )
        print("f - Full speed ahead")
        print("m - Moderate speed")
        print("s - Status")
        print("d - Drink")
        print("q - Quit")
 
user_command = get_user_choice()
print("You entered:", user_command)

