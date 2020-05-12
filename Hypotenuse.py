#import necessary portions of the math library
from math import sqrt 

#calculate hypotenuse
def ThirdSide(x, j):
    hypotenuse = sqrt(x**2 + j**2)
    return hypotenuse

#intake values of the sides 
def main():
    a = int(input("Enter the length of side a: "))
    b = int(input("Enter the length of side b: "))
    c = ThirdSide(a, b)
    print("The length of the hypotenuse (side c) is: %f  units" % c)

main()
    
#Other solution (just as a bonus because I came across this function online!) - my actual solution is the lines above
#I left this solution as a comment so it wouldn't interfere with my actual solution
"""from math import hypot

def otherSolution(x, y):
    third_side = hypot(x, y)
    return third_side

def otherMain():
    first_side = int(input("Entre the length of the first side: "))
    second_side = int(input("Entre the length of the second side: "))
    third_side = otherSolution(first_side, second_side)
    print("The length of the third side is: %d units" % third_side)
otherMain()"""
