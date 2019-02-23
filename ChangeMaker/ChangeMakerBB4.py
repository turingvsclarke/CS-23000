# VENDING MACHINE that allows the user to select and purchase several different entries and then runs the change-making process

# GUI in Python that will include products, prices and allow for user to buy products

# Print all the products available and their corresponding prices. Ask which product they want

products = ["laptop","cheeseburger","apple","phone","crackers","chips","candy bar","cookies","lollipop","limousine"]

product_cost = [495,2.40,1.19,240,3.15,1.50,2.18,1.19,1.20,20000]

keep_running = True

# Initiate variables so they don't have to be initiated within a conditional loop

selectionList = []

purchase_price = 0

cash_tendered = 0

product_number = 1


while keep_running:

    # Begin the program with an introduction to how the user should interact with the code

    print("Enter the numbers of each corresponding entry you want and hit ENTER after each one. Type FINISH when finished:")

    # Print and number all the available products

    for x in products:
        
        print(str(product_number) + ". " + x.capitalize() + " ",product_cost[products.index(x)])

        # Create a string of all acceptable numbers

        acceptable_products = "" + str(product_number)

        product_number = product_number + 1
        
    # Accept the number of the product that the user wants

    selection = input()

    # Keep accepting new selections until the user enters the command to terminate the entering process

    while selection!="FINISH" and selection!="finish":

        # checks to make sure that the product selected is a valid product, in the range of the products

        while selection.replace(" ","") not in acceptable_products:

            print("I'm sorry. That's not a valid item. Please try again.")

            selection = input()

        selected_product = int(selection)

        # adds the item to the user's list of products that they want to buy

        selectionList.append(selected_product)

        # takes new input

        selection = input()

    # Get a total price, matching each product with its corresponding cost in the cost list

    for y in selectionList:

        # add all the costs of the products together, rounding to two digits to avoid floating point issues 

        purchase_price = round((purchase_price) + (product_cost[y - 1]),2)

    # prints out how much the total cost is

    cash_tendered = float(input("The total is " + str(purchase_price) + ". Please enter how much you are going to pay as a decimal number: dollars.cents\n"))

    # Checks to make sure that the amount entered is at least as much as the cost

    while cash_tendered < purchase_price:

        # Ask the user for more money if they haven't paid enough money yet

        new_cash = round(input("You owe " + str(purchase_price - cash_tendered) + ". Please enter more money.\n"),2)

        # Accumulate the total amount paid

        cash_tendered = new_cash + cash_tendered

    # Print a receipt, including the tender history and products purchased

    print("Items purchased:")

    # print the name of every item purchased

    for z in selectionList:

        print(products[z-1].capitalize() + "                                          ",product_cost[z-1])    

    # Print the total cost and the paid amount

    print("Total: ",purchase_price)
    print("Cash tendered: ",cash_tendered)

    # Run the basic process to compute change

    # Take in the price of the item as before, multiplied by 100 to work in pennies

    price = float((purchase_price)*100)

    # Ask for the amount of cash tendered, multiply it by 100 to work in pennies

    cash = float((cash_tendered)*100)

    # compute the gross change

    change = cash - price

    # Let the user see how much change there is

    print("Change: ",change)

    # List for every denomination in English as singular and plural and quantitatively

    denominations_list = [2000,1000,500,100,25,10,5,1]

    denominations_plural = ["twenties","tens","fives","ones","quarters","dimes","nickels","pennies"]

    denominations_single = ["twenty","ten","five","one","quarter","dime","nickel","penny"]

    # Only run the operations to get change if there actually is change

    if change != 0:

        print("The change is as follows:")

        # Create a for loop that computes the amount of each denomination in the change using modular arithmetic

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

    # Print a receipt that has each item purchased, its price, total price, cash tendered, change back

    keep_running = False
