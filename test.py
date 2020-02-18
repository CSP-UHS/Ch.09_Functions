#import main
# def fizzbuzz(endpoint):
#     '''This fizzbuzz function'''
#     for i in range(1, endpoint+1):
#         if i%15==0:
#             print("FIZZBUZZ")
#         elif i % 5 == 0:
#             print("BUZZ")
#         elif i % 3 == 0:
#             print("FIZZ")
#         else:
#             print(i)
# def main():
#     fizzbuzz(100)
# if __name__ == "__main__":
#     main()

#################################
import random
import math
# def fibo(num):
#     a, b, c = 0, 1, 1
#     print(f"{0:>30,}")
#     for i in range(num):
#         print(f"{c:>30,}")
#         c = a + b
#         a=b
#         b=c
###############################################




#
# def main():
#     fibo(100)
#
# if __name__ == "__main__":
#     main()
#


###########################################
# def min(x, y, z):
#     if x<y and x<z:
#         return x
#     elif y<x and y<z:
#         return y
#     elif z<x and z<y:
#         return y
#     else:
#         return z
#
# print(min(7,3,5))
# print(min(5,5,4))
# print(min(2,2,3))
# print(min(-100,-6,-2))
# print(min("Z", "B","A"))
#

#######

# def box(h,w):
#     for i in range(h):
#         print("o"*w)
#
#
# box(7,5)
# print()
# box(3,2)

###############
# def find(list, key):
#     pos = 0
#     for item in list:
#         if item ==key:
#             print("found", key, "at position", pos)
#         pos+=1
#
# list = [36, 31, 79, 96, 36,]
#
########################################

#YAZI
import random
def create_list(n):
   list = []
   for i in range(n):
       var=random.randint(1,6)
       list.append(var)
   return list
# print(create_list(5))

####################
def count_list(list, num):
   count=0
   for item in list:
       if item == num:
           count+=1
   return count


#
# my_list = [1, 2, 3 , 3,3, 4, 2, 1,]
# count = count_list(my_list, 4)
# print(count)

#####################################################


def average_list(list):
   total=0
   for item in list:
       total+=item
   avg=total/len(list)
   return f"{avg:.2f}"
# my_list = [1,2,3]
# avg = average_list(my_list)
# print(avg)
############################################
# def main():
#     my_list=create_list(10000)
#     for i in range(1, 7):
#         count=count_list(my_list, i)
#         print("There are", count, "number of", i,"s!")
#     print()
#     print(average_list(my_list))
#
# if __name__=="__main__":
#     main()


#################################################
# '''
# BB8 DRAWING PROGRAM
# -------------------
# Back to the drawing board! Get it? Let's say we want to draw many BB8 robots
# of varying sizes at various locations. We can make a function called draw_BB8().
# We've made some basic changes to our original drawing program. We still have the
# first two lines as importing arcade and opening an arcade window. We actually took
# all of the other drawing code and put it in a function called main(). At the bottom
# we call the main() function. In the main() function we call the draw_BB8() function
# multiple times. We pass three parameters to it: x, y and radius. Write the code for
# the draw_BB8() function so that the resulting picture looks as close as you can get
# it to the one on the website.
# '''
#
# # Imports arcade module
# import arcade
#
# # Opens a 600px by 600px window and puts BB8 in the title
# arcade.open_window(600, 600, "BB8")
#
#
# # Function to draw BB8 robots
# def draw_BB8(x, y, radius):
#
#
# #The main function where we set background color, start and finish rendering and run.
# def main():
#     arcade.set_background_color(arcade.color.WHEAT)
#     arcade.start_render()
#
#     draw_BB8(100, 50, 50)
#     draw_BB8(300, 300, 30)
#     draw_BB8(500, 100, 20)
#     draw_BB8(500, 400, 60)
#     draw_BB8(120, 500, 15)
#
#     arcade.finish_render()
#     arcade.run()
#
#
# # Calls the main function
# main()
#
# #calls the main function
# if __name__ == "__main__":
#     main()

####################################
#JEDI TRAINING
# #1)
# def increase(x):
#     return x+1
# num = int(input("Enter a number:"))
# num2 = increase(num)
# print("Your number has been increased to", num2)
#

#2)
# def count_to_ten():
#     for i in range(1,11):
#         print(i)
# count_to_ten()

#3)
###SOMETHING WRONG WITH THIS ONE###
# def sum_list(list):
#     sum=0
#     for i in list:
#         sum+=1
#     return sum
# list = [45,2,10,-5,100]
# print(sum_list(list))




#4)

#####WSOMETHING WRONG LMAO#########
# def reverse(text):
#     result = ""
#     text_length = len(text)
#     for i in range(text_length):
#         result = result + text[i*-1-1]
#     return result
# text = input("Enter a sentence: ")
# print(reverse())



#5)
# 5.) Correct the following code: (if one of the options is not entered it should print the statements)


def get_user_choice():
   while True:
       command = input("Command: ")
   if command == "f" or command == "m" or command == "s" or command == "d" or command == "q":
       return command
   else:
       print("Hey, that's not a command. Here are your options:")
       print("f - Full speed ahead")
       print("m - Moderate speed")
       print("s - Status")
       print("d - Drink")
       print("q - Quit")

user_command = get_user_choice()

print("You entered:", user_command)


# if __name__ == "__main__":
#     main()
#
################################################






