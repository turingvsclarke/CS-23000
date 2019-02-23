# A program that computes how much change you owe after you pay for something

# Take in the price of the item as before, multiplied by 100

purchase_price = float(input("How much did the item cost?\n"))*1000

# Ask for the amount of cash tendered, multiply it by 100

cash_tendered = (float(input("How much cash was paid?\n"))*1000)

# Calculate the change in pennies. Note that this assumes they paid enough money

change = cash_tendered - purchase_price

# Quantitative denominations list and singular/plural denominations descriptors

denominations_list = [20000,10000,5000,1000,250,100,50,10]

denominations_plural = ["twenties","tens","fives","ones","quarters","dimes","nickels","pennies"]

denominations_single = ["twenty","ten","five","one","quarter","dime","nickel","penny"]

# Tell the user that the amount of change will soon be outputed 

print("The change is as follows:")

# Create a for loop that removes multiples of the denominations for each one in our list

for x in denominations_list:

    # Use the same modular formula as before

    denomination_quantity = int((change-(change%x))/x)

    change = change%x

    # Store each result in a string of change denominations, as long as it's non-empty

    if denomination_quantity!=0:

        # Use singular denominations list for singular change

        if denomination_quantity==1:

            # Print number and type of each denomination

            print(str(denomination_quantity) + " " + denominations_single[denominations_list.index(x)] + ".")

        # Use plural denominations list for plural change

        else:

            # Print number and type of each denomination

            print(str(denomination_quantity)+ " " + denominations_plural[denominations_list.index(x)]+".")
