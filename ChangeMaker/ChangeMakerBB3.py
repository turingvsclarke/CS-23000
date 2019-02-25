# A program that computes how much change you owe after you pay for something
# All of this will now be wrapped up in a GUI designed to replicate a vending machine


# It now will include 10 different products that the user will buy 
# It should also now include flags for the user not paying enough money


# List of items and a list with corresponding prices




# Take in the price of the item as before, multiplied by 100

purchase_price = float(input("How much did the item cost?\n"))*100

# Ask for the amount of cash tendered, multiply it by 100

cash_tendered = (float(input("How much cash was paid?\n"))*100)

# Calculate the change in pennies. Note that this assumes they paid enough money

change = cash_tendered - purchase_price

# Create a for loop that takes the modulus for each number in a list of denominations

denominations_list = [2000,1000,500,100,25,10,5,1]

denominations_plural = ["twenties","tens","fives","ones","quarters","dimes","nickels","pennies"]

denominations_single = ["twenty","ten","five","one","quarter","dime","nickel","penny"]

# Empty change denominations string

print("The change is as follows:")

for x in denominations_list:

    # Use the same modular formula as before

    denomination_quantity = int((change-(change%x))/x)

    change = change%x

    # Store each result in a string of change denominations, as long as it's non-empty

    if denomination_quantity!=0:

        # Use singular denominations list for singular change

        if denomination_quantity==1:

            print(str(denomination_quantity) + " " + denominations_single[denominations_list.index(x)] + ".")

        # Use plural denominations list for plural change

        else:

            print(str(denomination_quantity)+ " " + denominations_plural[denominations_list.index(x)]+".")
