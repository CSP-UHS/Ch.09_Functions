#Sign your name: Ryan Mullins


#1.) Correct the following code: (The user's number should be increased by 1 and printed.)

def increase(x):
    new_num = x+1
    print("Your number has been increased to",new_num)
    return new_num

num = int(input("Enter a number: "))
increase(num)

                        
 


#2.) Correct the following code to print 1-10:

def count_to_ten():
    for i in range(1,11):
        print(i)

count_to_ten()



#3.) Correct the following code to sum the list:


def sum_list(list):
    x = 0
    for item in list:
        x += item
    print(x)

list = [45, 2, 10, -5, 100]
sum_list(list)




#4.) Correct the following code which should reverse the sentence that is entered.

def reverse(text):
    result = text[::-1]
    print(result)

text = input("Enter a sentence: ")
reverse(text)



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

