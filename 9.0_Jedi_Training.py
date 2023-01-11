#Sign your name: Oded Harazi


#1.) Correct the following code: (The user's number should be increased by 1 and printed.)

def increase(x):
    sum = x + 1
    print("Your number has been increased to", sum)

x = int(input("Enter a number: "))
x = increase(x)


#

#2.) Correct the following code to print 1-10:

def count_to_ten():
    for i in range(1,11):
        print(i)

count_to_ten()



#3.) Correct the following code to sum the list:

def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum
 
list = [45, 2, 10, -5, 100]
print(sum_list(list))




#4.) Correct the following code which should reverse the sentence that is entered.

def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[(i+1) * -1]
    return result

text = input("Enter a sentence: ")
print(reverse(text))



#5.) Correct the following code: (if one of the options is not entered it should print the statements)

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

