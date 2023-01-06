def mean(x,y,z):
    ave=(x+y+z)/3.0
    print(ave)

def hyp(leg1,leg2):
    hypo = (leg1**2 + leg2**2)**.5
    print(f"{hypo:.2f}")

def volsph(r):
    volume =4/3*3.14*r**3
    print(f"{volume:.2f}")

def volsph2(r):
    volume =4/3*3.14*r**3
    return volume

def volcyl(r,h):
    volume = h*3.14*r**2
    print(f"{volume:.2f}")

def printHello():
    ''' This function prints hello '''
    print("Hello")

def printGoodbye():
    print("Goodbye")

def math():
    volcyl(2, 3)
    volume = volsph2(5)
    volsph(5)
    print(volume)

def main():
    printHello()
    printGoodbye()

if __name__ == "__main__":
    main()

hyp(2,3)