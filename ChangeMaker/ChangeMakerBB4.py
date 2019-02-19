# Possible option that allows the user to enter several different entries and then runs the change-making process

# GUI in Python that will include products, prices and allow for user to buy products

# Print all the products available and their corresponding prices. Ask which product they want

products = ["laptop","cheeseburgeer","apple","phone","crackers","chips","candy bar","cookies","lollipop","limousine"]

product_cost = [495,2.40,1.19,240,3.15,1.50,2.18,1.19,1.20,20000]

keep_running = True

# Initiate a list for product selection

selectionList = []

purchase_price = 0

cash_tendered = 0

product_number = 1

while keep_running:

    print("Enter the numbers of each corresponding entry you want and hit ENTER after each one. Type FINISH when finished:")

    # Print and number all the available products

    for x in products:
        print(str(product_number) + ". " + x.capitalize() + " ",product_cost[products.index(x)])

        product_number = product_number + 1

    # Accept the number of the product that the user wants

    selection = input()

    # Keep accepting new selections until the user enters the command to terminate the entering process

    while selection!="FINISH" and selection!="finish":

        # checks to make sure that the product selected is a valid product, within length of list and an integer

     #if selected_product < 1 or selected_product > len(products):

      #   selection = input("I'm sorry. That's not a valid item. Please try again.\n") """

        # converts the selected item to integers ''' 

        selected_product = int(selection)

        # adds the item to the user's list of products that they want to buy

        selectionList.append(selected_product)

        # takes new input

        selection = input()

    # assigns the price to the entry in the price list with the corresponding

    # add the cost of each individual product together

    for y in selectionList:

        # add all the costs of the products together

        purchase_price = purchase_price + product_cost[y - 1]

    # prints out how much the total cost is

    cash_tendered = float(input("The total is " + str(purchase_price) + ". Please enter how much you are going to pay as a decimal number: dollars.cents\n"))

    # Checks to make sure that the amount entered is at least as much as the cost

    while cash_tendered < purchase_price:

        new_cash = float(input("You owe " + str(purchase_price - cash_tendered) + ".\n"))

        cash_tendered = new_cash + cash_tendered


    print("Items purchased:")

    for z in selectionList:

        print(z, "                                          ",product_cost[z-1])    

    print("Total: ",purchase_price)
    print("Cash tendered: ",cash_tendered)

    # Now run the process to compute change

    # Take in the price of the item as before, multiplied by 100

    price = float((purchase_price)*100)

    # Ask for the amount of cash tendered, multiply it by 100

    cash = float((cash_tendered)*100)

    change = cash - price

    # Create a for loop that takes the modulus for each number in a list of denominations

    denominations_list = [2000,1000,500,100,25,10,5,1]

    denominations_plural = ["twenties","tens","fives","ones","quarters","dimes","nickels","pennies"]

    denominations_single = ["twenty","ten","five","one","quarter","dime","nickel","penny"]

    # Empty change denominations string

    print("Change: ",change)

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

    # Print a receipt that has each item purchased, its price, total price, cash tendered, change back

    keep_running = False
