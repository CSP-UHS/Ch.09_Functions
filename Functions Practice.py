import math

#def volume_sphere(radius):
    #volume=4/3*math.pi(radius,3)
    #return volume

def hyp(leg1,leg2):
    hypot=math.sqrt(leg1**2 + leg2**2)
    print(hypot)

def volume_cyl(r,h):
    volume=4/3*math.pi*math.pow(r,2)*h
    return volume

def mean(list):
    total=0
    for item in list:
        total+=item
    avg = total/len(list)
    print(avg)

def perimeter(b,h):
    per=2*b+2*h
    print(per)

def myprogram():
    hyp(1,2)
    numlist=[13,2,54,23,34,71]
    mean(numlist)
    perimeter(4,5)



print(__name__)
if __name__=="__main___":
    myprogram()

