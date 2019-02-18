# Possible option that allows the user to enter several different entries and then runs the change-making process

# GUI in Python that will include products, prices and allow for user to buy products

# Print all the products available and their corresponding prices. Ask which product they want

# Now is an infinite loop that always shows the menu. Basically only handles one item at once


# ASSUMES THERE IS A LIST CALLED products AND A LIST CALLED product_cost

keep_running = True

# Initiate a list for product selection

selectionList = []

price = 0

while keep_running:

    print("Enter the numbers of each corresponding entry you want and hit ENTER after each one. Type FINISH when finished:")

    # Initialize the labelling for numbering the product options

    product_number = 1

    collected_cash = 0

    # Print and number all the available products

    for x in products:
        print(product_number, ". " + x.capitalize() + " " + product_cost[products.index(x)])

        product_number = product_number + 1

    # Accept the number of the product that the user wants

    selection = input()

    # Keep accepting new selections until the user enters the command to terminate the entering process

    while selection!=="FINISH":

        # convert the input to integers

        selected_product = int(input())

        # checks to make sure that the product selected is a valid product

        while selected_product < 1 or selected_product > products.len():

            print("I'm sorry. That's not a valid item. Please try again.")

            selection = input()

        selectionList.append(selected_product)

    # assigns the price to the entry in the price list with the corresponding

    # add the cost of each individual product together

     for y in selectionList:

        # add all the costs of the products together

        price = price + product_cost[y - 1]

    # prints out how much the total cost is

    collected_cash = int(input("The total is " + str(price) + ". Please enter how much you are going to pay as a decimal number: dollars.cents\n"))

    # Checks to make sure that the amount entered is at least as much as the cost

    while collected_cash < price

        new_cash = input("You owe ", price - collected_cash, ".\n")

        collected_cash = new_cash + collected_cash

    # Now run the process to compute change



    # Print a receipt that has each item purchased, its price, total price, cash tendered, change back

    print("Items purchased:")

    for z in selectionList

        print(z, "                                          " + product_cost[z-1])

    print("Total: ",price)
    print("Cash tendered: ",collected_cash)

    print("Change: ",change)

