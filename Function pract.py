import math
a = 2
def volume_sphere(radius):
    ''' This function calcualtes the volume of a sphere '''
    volume = 4/3*math.pi*math.pow(radius,3)
    print(f"Thw volume is {volume:.2f} in^3")


def volume_cyl(r,h):
    volume = math.pi*math.pow(r,2)
    return volume
def hyp(leg1,leg2):
    hypot= math.sqrt(leg1**2 + leg2**2)
    print(hypot)
def mean(list):
    total = 0
    for item in list:
        total += item
    avg = total/len(list)
    print(avg)

def myprogram():
    hyp(1,2)
    mean(12)

if __name__ == "__main__":
    myprogram()