# Hypotenuse Function
def hyp(leg1,leg2):
    hypo = (leg1**2 + leg2**2)**.5
    print(hypo)


# Mean Function
def mean(x,y,z):
    ave = (x+y+z)/3.0
    print(ave)


# Perimeter Function
def rect(b,h):
    per=2*b+2*h
    print(per)




def main():
    hyp(2,3)
    mean(1,7,22)
    rect(3,4)

if __name__ == "__main__":
    main()
