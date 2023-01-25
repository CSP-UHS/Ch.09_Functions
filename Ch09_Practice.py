"""
def volume_sphere(radius):
    volume = 4 / 3 * 3.14 * radius ** 3
    return volume


vol = volume_sphere(1)
print(f"The volume is {vol:.2f}")  # volume in this line needs to be redefined because it's not included with the
# volume_sphere function
print("--------------------")


def volume_cylinder(r, h):
    volume = h * 3.14 * r ** 2
    return volume


vol = volume_cylinder(2, 3)
print(f"The volume is {vol:.2f}")


def main():
    vol = volume_cylinder(2, 3)
    print(f"The volume is {vol:.2f}")


main()
print("-------------------------------")


def print_hello():
    #This function prints hello
    print("Hello!!!!")


def print_goodbye():
    print("Goodbye!!!!")


def main():
    help(print_hello)  # prints what it says in the docstrings


if __name__ == "__main__":
    main()
print("-------------------------------")


def hyp(leg1,leg2):
    hypo = (leg1**2 + leg2**2) **0.5
    print(hypo)

    
def main():
    hyp(2,3)

if __name__ == "__main__":
    main()
print("-------------------------------")

def mean(x,y,z):
    ave=(x+y+z)/3.0
    print(ave)


def main():
    mean(1,7,22)


if __name__ == "__main__":
    main()



def rect(b,h):
    per = 2*b+2*h
    print(per)


def main():
    rect(3,4)


if __name__ == "__main__":
    main()
print("--------------------")
"""
print()
