# VENDING MACHINE that allows the user to select and purchase several different entries and then runs the change-making process, which now includes 100 bills
# This could be modified for any number of products and corresponding prices, as long as they are added to the respective lists at the same index

# Print all the products available and their corresponding prices. Ask which product they want

products = ["laptop","cheeseburger","apple","phone","crackers","chips","candy bar","cookies","lollipop","limousine"]

product_cost = [495,2.40,1.19,240,3.15,1.50,2.18,1.19,1.20,20000]

keep_running = True

# Initiate variables so they don't have to be initiated within a conditional loop

selectionList = []

purchase_price = 0

acceptable_products = ""

cash_tendered = 0

product_number = 1

while keep_running:

    # Begin the program with an introduction to how the user should interact with the code

    print("Enter the numbers of each corresponding entry you want and hit ENTER after each one. Type FINISH when finished:")

    # Print and number all the available products

    for x in products:
        
        print(str(product_number) + ". " + x.capitalize() + " ",product_cost[products.index(x)])

        # Create a string of all acceptable numbers

        acceptable_products = acceptable_products + " " + str(product_number)

        # Assign the next product the next number

        product_number = product_number + 1
        
    # Accept the number of the product that the user wants

    selection = input()

    # Keep accepting new selections until the user enters the command to terminate the entering process

    while selection!="FINISH" and selection!="finish":

        # checks to make sure that the product selected is a valid product, in the range of the products

        if selection.replace(" ","") not in acceptable_products or selection.replace(" ","")=="":

            # tell the user that the input is invalid

            print("I'm sorry. That's not a valid item. Please try again.")

            # take another input

            selection = input()

        else:

            # convert the input to integers if it is an acceptable input
        
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

    cash_tendered = round(float(input("The total is " + str(purchase_price) + ". Please enter how much you are going to pay as a decimal number: dollars.cents\n")),2)

    # Checks to make sure that the amount entered is at least as much as the cost

    while cash_tendered < purchase_price:

        # Ask the user for more money if they haven't paid enough money yet

        new_cash = round(float(input("You owe " + str(purchase_price - cash_tendered) + ". Please enter more money.\n")),2)

        # Accumulate the total amount paid

        cash_tendered = new_cash + cash_tendered

    # Print a receipt, including the tender history and products purchased

    print("Items purchased:")

    # print the name of every item purchased

    for z in selectionList:

        # Print each product left justified and each cost right justified

        print("{:<20}{:>10}".format(products[z-1].capitalize(),product_cost[z-1]))

    # Print the total cost and the paid amount, right justified"

    print("Total: ",purchase_price)
    print("Cash tendered: ",cash_tendered)

    # Run the basic process to compute change

    # Like before, covert the change to be represented in pennies by multiplying the change by 100

    change = round(float((cash_tendered - purchase_price)*100),2)

    # Print out the change

    print("Change: ",round(float(cash_tendered-purchase_price),2))

    # List for every denomination in English as singular and plural and quantitatively

    denominations_list = [10000,2000,1000,500,100,25,10,5,1]

    denominations_plural = ["hundreds", "twenties","tens","fives","ones","quarters","dimes","nickels","pennies"]

    denominations_single = ["hundred","twenty","ten","five","one","quarter","dime","nickel","penny"]

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
    
    # make the while loop end for now

    keep_running = False
