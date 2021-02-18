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

list = [1]


def fibonacci(a):
    if a <= 100:
        b = a
    else:
        b = 100
    while len(list) < b:
        list.append(list[-1] + list[-2])
    print(list)


def fibi(num):
    x, y = 1, 1
    for i in range(num):
        z = x+y
        y = x
        x = z
        print(f"{z:>50}")

def main():
    fibi(12)


if __name__ == "__main__":
    main()