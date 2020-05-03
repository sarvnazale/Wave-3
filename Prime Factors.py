#ask for user input
number = int(input("Enter a number (must be greater than 2): "))

#check that number is greater than 2 
if number < 2:
    raise Exception('Input should not be less than 2. The value of the input was: {}'.format(number))

#start with the lowest prime number
factor = 2

#calculate the prime factors
while factor <= number:
    if number % factor == 0:
        print(factor)
        number = number // factor 
    else:
        factor += 1



