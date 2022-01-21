'''
FIBONACCI
---------
In mathematics, the Fibonacci numbers are the numbers in the following integer sequence, 
called the Fibonacci sequence, and characterized by the fact that every number after the
first two is the sum of the two preceding ones:1,1,2,3,5,8,13,21,34,55,89,144
Write a function called fibonacci() that will print up to a maximum of the first 100 numbers
in the Fibonacci sequence. Pass the number into the function.

Just to do a quick review of text formatting in the last chapter, make the list of numbers
right-justified with commas.
'''
def Fibonacci():
    b=1
    a=0
    sum=a+b
    n=1
    x=11
    for i in range(99):
        print(f"{sum:50,}")
        a=b
        b=sum
        sum=a+b
def myprogram():
    Fibonacci()
if __name__=="__main__":
    myprogram()

