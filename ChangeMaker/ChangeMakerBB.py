# GUI in Python that will include products, prices and allow for user to buy products

# Print all the products available and their corresponding prices. Ask which product they want

# Now is an infinite loop that always shows the menu. Basically only handles one item at once

keep_running = True

while keep_running:

    print("Which object would you like to buy? Here are your options and their prices. Enter the number corresponding to the entry you want:")

    # Initialize the labelling for numbering the product options

    product_number = 1

    collected_cash = 0

    # Print and number all the available products

    for x in products:

        print(product_number,". " + x.capitalize() + " " + product_cost[x.index()])

        product_number = product_number + 1

    # Accept the number of the product that the user wants

    selected_product = int(input() + "\n")

    # checks to make sure that the product selected is a valid product

    while selected_product < 1 or selected_product > products.len():

        print("I'm sorry. That's not a valid item. Please try again.")

        selected_product = int(input() + "\n")

    # assigns the price to the entry in the price list with the corresponding

    price = product_cost[selected_product - 1]

    # prints out how much the item costs

    print("That costs",price)

    # Checks to make sure that the amount entered is at least as much as the cost

    while collected_cash < price

        new_cash = input("You owe ",price - collected_cash,".\n")

        collected_cash = new_cash + collected_cash























