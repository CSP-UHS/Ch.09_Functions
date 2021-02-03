import random

def hypotenuse (a,b):
    h = (a**2+b**2)**.5
    print(f"The hypotenuse is {h:.2f}")

def mean(a,b,c):
    ave = (a+b+c)/3
    print(f"The average is {ave:.2f}")

def perimeter (b,h):
    per = b*h
    print (f"The area of the rectangle was {per:.2f}")

def myprogram():
    '''This is my main program'''
    hypotenuse(3,4)
    mean(3,7,23)
    perimeter(10,3)

if __name__ == "__main__":
    myprogram()


#help(myprogram)

