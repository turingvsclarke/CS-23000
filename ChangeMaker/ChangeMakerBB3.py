# GUI in Python that will include products, prices and allow for user to buy products

# Print all the products available and their corresponding prices. Ask which product they want

print("Which object would you like to buy? Here are your options and their prices. Enter the number corresponding to the entry you want:")

# Initialize the labelling for numbering the product options

product_number = 1

# Print and number all the available products

for x in products:

    print(product_number,". " + x.capitalize() + " " + product_cost[x.index()])

    product_number = product_number + 1

# Accept the number of the product that the user wants

selected_product = int(input())



while selected_product < 1 or selected_product > products.len():

    print("I'm sorry. That's not a valid item. Please try again.")

    selected_product = int(input())

price = product_cost[selected_product - 1]






#





















