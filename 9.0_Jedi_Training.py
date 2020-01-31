#Sign your name:Malsawmthara Hmar


#1.) Correct the following code: (The user's number should be increased by 1 and printed.)

def increase(x):
    return x + 1
 
num = int(input("Enter a number: "))
num2=increase(num)
print("Your number has been increased to", num2)
                        
 


#2.) Correct the following code to print 1-10:

def count_to_ten():
    for i in range(10):
        print(i)
 
count_to_ten()



#3.) Correct the following code to sum the list:

def sum_list(list):
    total=0
    for item in list:
        sum = total+item
    return sum
 
list = [45, 2, 10, -5, 100]
print(sum_list(list))




#4.) Correct the following code which should reverse the sentence that is entered.

def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result = result + text[i * -1]
    return result
 
text = input("Enter a sentence: ")
print(reverse(text))



#5.) Correct the following code: (if one of the options is not entered it should print the statements)

def get_user_choice():
    done=False
    while not done:
        command = input("Command: ")
        if command.lower() == "f":
            print("f - Full speed ahead")
        elif command.lower() == "m":
            print("m - Moderate speed")
        elif command.lower() == "s":
            print("s - Status")
        elif command.lower() == "d":
            print("d - Drink")
        elif command.lower() == "q":
            print("q - Quit")
            done=True
        else:
            print("Hey, that's not a command. Here are your options:")
            print("f - Full speed ahead")
            print("m - Moderate speed")
            print("s - Status")
            print("d - Drink")
            print("q - Quit")
        return command
 
user_command = get_user_choice()
print("You entered:", user_command)

