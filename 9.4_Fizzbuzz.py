'''
FIZZBUZZ
--------
The "Fizz-Buzz test" is an interview question designed to help filter out the 99.5% 
of programming job candidates who can't seem to program their way out of a wet paper bag.
Write a function called fizzbuzz that prints the numbers from 1 to "endpoint", where 
endpoint is your final number. But for multiples of three print "Fizz" instead of the
number and for the multiples of five print "Buzz". For numbers which are multiples of
both three and five print "FizzBuzz". Once you've finished writing your function, 
copy and paste the following code after it and make sure it works with the function you wrote:

INPUT
-----
fizzbuzz(15)

OUTPUT
------
1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz


The classic test is to use the numbers 1-100 so make sure you test that with your function.
'''


def fizzbuzz(a):
    x = 0
    t = 3
    f = 5
    ft = 15
    for y in range(a):
        x += 1
        if x == ft:
            print("fizzbuzz")
            ft += 15
            f += 5
            t += 3
        elif x == f:
            print("buzz")
            f += 5
        elif x == t:
            print("fizz")
            t += 3
        else:
            print(x)


fizzbuzz(100)
