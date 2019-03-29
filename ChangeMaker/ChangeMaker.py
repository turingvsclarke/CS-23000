# A program that computes how much change you owe after you pay for something

# Ask for a purchase price, multiply it by 100

purchase_price = int(float(input("How much did the item cost?\n"))*100)

# Ask for the amount of cash tendered, multiply it by 100

cash_tendered = int(float(input("How much cash was paid?\n"))*100)

# Calculate the change in pennies. Note that this assumes they paid enough money

change = cash_tendered - purchase_price

# Determine how many twenties are due by subtracting the modulus from cash-tendered and dividing by 2000

number_of_twenties = (change-(change%2000))/2000

# Reset the change

change = change%2000

# Determine how many tens are due by subtracting the modulus from cash-tendered and dividing by 1000

number_of_tens = (change-(change%1000))/1000

change = change%1000

# Determine how many fives are due by subtracting the modulus from cash-tendered and dividing by 500

number_of_fives = (change-(change%500))/500

change = change%500

# Determine how many ones are due by subtracting the modulus from cash-tendered and dividing by 100

number_of_ones = (change-(change%100))/100

change = change%100

# Determine how many quarters are due by subtracting the modulus from cash-tendered and dividing by 25

number_of_quarters = (change-(change%25))/25

change = change%25

# Determine how many dimes are due by subtracting the modulus from cash-tendered and dividing by 10

number_of_dimes = (change-(change%10))/10

change = change%10

# Determine how many nickels are due by subtracting the modulus from cash-tendered and dividing by 5

number_of_nickels = (change-(change%5))/5

change = change%5

# The remaining change is the number of pennies

number_of_pennies = change

# Print the change by denomination

print("The change is as follows:")
print(number_of_twenties," twenties.")
print(number_of_tens," tens.")
print(number_of_fives," fives.")
print(number_of_ones," ones.")
print(number_of_quarters," quarters.")
print(number_of_dimes," dimes.")
print(number_of_nickels," nickels.")
print(number_of_pennies," pennies.")