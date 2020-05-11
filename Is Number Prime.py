
#function that determines whether number is prime
def isPrime(j):
    for i in range(2, j):
        if j % i == 0:
            return False
        elif j <= 1:
            return False
        else:
            return True

#main function that intakes the number and calls on the prime function
def main():
    number = int(input("Enter an integer to see if it prime: "))
    if isPrime(number) == True:
        print("%d is a prime number." % number)
    else:
        print("%d is not a prime number." % number)

#Ensures program will not run if file containing solution is imported into another program
if __name__ == "__main__":
    main()   
