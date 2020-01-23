# Sign your name:_Kenny Flory

'''
# 1.) Correct the following code: (The user's number should be increased by 1 and printed.)

def increase(x):
    return x+1
 
num = int(input("Enter a number: "))
new=increase(num)
print("Your number has been increased to", new)

 


#2.) Correct the following code to print 1-10:

def count_to_ten():
    for i in range(11):
        print(i)
 
count_to_ten()



# 3.) Correct the following code to sum the list:
def sum_list(list):
    sums = 0
    for item in list:
        sums += item
    return sums


old = [45, 2, 10, -5, 100]
total=sum_list(old)
print(total)

# 4.) Correct the following code which should reverse the sentence that is entered.

def reverse(text):
    result = ""
    text_length = len(text)
    for i in range(text_length):
        result += text[(i+1) * -1]
    return result


text = input("Enter a sentence: ")
new=reverse(text)
print(new)



#5.) Correct the following code: (if one of the options is not entered it should print the statements)

def get_user_choice():
    while True:
        command = input("Command: ")
        if command.lower()=="f" or command.lower()=="m" or command.lower()=="s" or command.lower()=="d"\
                or command.lower() == "q":
            return command
        else:
            print()
            print("Hey, that's not a command. Here are your options:" )
            print("f - Full speed ahead")
            print("m - Moderate speed")
            print("s - Status")
            print("d - Drink")
            print("q - Quit")
 
user_command = get_user_choice()
print()
print("You entered:", user_command)
'''
