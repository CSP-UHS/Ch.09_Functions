#Sign your name: Emma E. Moritz

'''
#1.) Correct the following code: (The user's number should be increased by 1 and printed.)

def increase(x):
    return x + 1

num = int(input("Enter a number: "))
y=increase(num)
print("Your new number is: "y)



#2.) Correct the following code to print 1-10:

def count_to_ten():
    for i in range(1,11):
        print(i)
count_to_ten()




#3.) Correct the following code to sum the list:
def sum_list(list):
    sum=0
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
        result = result + text[i * -1-1]
    return result
 
text = input("Enter a sentence: ")
print(reverse(text))
'''

#5.) Correct the following code: (if one of the options is not entered it should print the statements)

def get_user_choice():
    while True:
        command = input("Command: ")
        if command.lower() == "f" or command.lower() == "m" or command.lower() == "s" or command.lower() == "d" or command.lower() == "q":
            return command
        else:
            print("Hey, that's not a command. Here are your options:" )
            print("f - Full speed ahead")
            print("m - Moderate speed")
            print("s - Status")
            print("d - Drink")
            print("q - Quit")
 
user_command = get_user_choice()
print("You entered:", user_command)

















