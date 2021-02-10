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


def fizzbuzz(rnge):
    for i in range(1, rnge+1):
        t3 = str(i/3)
        t5 = str(i/5)
        for l in range(len(t3)):
            if t3[l] == ".":
                strt3 = l+1
        for k in range(len(t5)):
            if t5[k] == ".":
                strt5 = k+1
        if t3[strt3] == "0" and t5[strt5] == "0":
            print("fizzbuzz")
        elif t3[strt3] == "0":
            print("fizz")
        elif t5[strt5] == "0":
            print("buzz")
        else:
            print(i)


def main():
    fizzbuzz(100)


if __name__ == "__main__":
    main()
