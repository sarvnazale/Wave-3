#calculate shipping
def ShippingCalculator(x):
    shipping = 10.95 + ((x-1) * 2.95)
    return shipping

#Main function that takes in input
def Main():
    num_items = int(input("How many items have you ordered? "))
    cost = ShippingCalculator(num_items)
    print("Your total shipping cost is: %d dollars" % cost)

Main()
