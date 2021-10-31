
# Functions (checks if the input for the budget is a number (float or integer))
def number_check(question, low, high):
    valid = False
    while not valid:
        error = "Please enter you budget again (Incorrect input)".format(low, high)
        try:
            response = float(input("Enter your budget (e.g $15.60)? $"))
            if 1 <= response <= 1000:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# To make the output look nice
print()

# Printing program name
print("PRICE COMPARISON TOOL")

# To make the output look nice
print()

# Header to tell the user what to do
print(" *** INSTRUCTIONS *** ")

# To make the output look nice
print()

# To tell the user what to do
print("Answer the questions as the computer tells you too. Clicking the <enter> key when you are done with that "
      "question to move on to the next done question.")
print("After you have answered all of the questions you will presented with table that will show you all the "
      "information that you have entered.")
print("And some computer generated numbers there as well. The computer will also recommend which of your "
      "entered products you should buy based of the unit price per kilogram.")

# To make the output look nice
print()

# Asks the user what their budget is
budget = number_check("Enter your budget (e.g 15)? ", 1, 1000)

# Gives the feedback from their budget input
print("Your budget is: ${:.2f}".format(budget))

# Defines the budget variable as a float
float(budget)

# Names of products (inputted as a string)
product_1_name = input("What is the name of this product? ").title()
product_2_name = input("What is the name of this product? ").title()
product_3_name = input("What is the name of this product? ").title()
product_4_name = input("What is the name of this product? ").title()
product_5_name = input("What is the name of this product? ").title()
product_6_name = input("What is the name of this product? ").title()


# Weights of products in Grams (inputted as a integer)
product_1_weight_g = int(input("What is the weight of the {} in grams (e.g. 638)? ".format(product_1_name)))
product_2_weight_g = int(input("What is the weight of the {} in grams (e.g. 638)? ".format(product_2_name)))
product_3_weight_g = int(input("What is the weight of the {} in grams (e.g. 638)? ".format(product_3_name)))
product_4_weight_g = int(input("What is the weight of the {} in grams (e.g. 638)? ".format(product_4_name)))
product_5_weight_g = int(input("What is the weight of the {} in grams (e.g. 638)? ".format(product_5_name)))
product_6_weight_g = int(input("What is the weight of the {} in grams (e.g. 638)? ".format(product_6_name)))

# Converting grams to kilograms (divide by 1000)
product_1_weight_kg = product_1_weight_g / 1000
product_2_weight_kg = product_2_weight_g / 1000
product_3_weight_kg = product_3_weight_g / 1000
product_4_weight_kg = product_4_weight_g / 1000
product_5_weight_kg = product_5_weight_g / 1000
product_6_weight_kg = product_6_weight_g / 1000

# Product Cost (inputted as a float)
product_1_cost = float(input("What is the cost of {} (enter like the ticket price, e.g. $12.50)? $".format
                             (product_1_name)))

product_2_cost = float(input("What is the cost of {} (enter like the ticket price, e.g. $12.50)? $".format
                             (product_2_name)))

product_3_cost = float(input("What is the cost of {} (enter like the ticket price, e.g. $12.50)? $".format
                             (product_3_name)))

product_4_cost = float(input("What is the cost of {} (enter like the ticket price, e.g. $12.50)? $".format
                             (product_4_name)))

product_5_cost = float(input("What is the cost of {} (enter like the ticket price, e.g. $12.50)? $".format
                             (product_5_name)))

product_6_cost = float(input("What is the cost of {} (enter like the ticket price, e.g. $12.50)? $".format
                             (product_6_name)))

# Unit Price by the kilogram (using division)
product_1_unit_price = product_1_cost / product_1_weight_kg
product_2_unit_price = product_2_cost / product_2_weight_kg
product_3_unit_price = product_3_cost / product_3_weight_kg
product_4_unit_price = product_4_cost / product_4_weight_kg
product_5_unit_price = product_5_cost / product_5_weight_kg
product_6_unit_price = product_6_cost / product_6_weight_kg

print()

# Print statements that print the users inputs and computer generated ones all at once
print("{}:  Weight: {} grams    Weight: {:.3f} kilograms    Cost: ${:.2f}   Unit Price: ${:.2f}".format
      (product_1_name, product_1_weight_g, product_1_weight_kg, product_1_cost, product_1_unit_price))

print("{}:  Weight: {} grams    Weight: {:.3f} kilograms    Cost: ${:.2f}   Unit Price: ${:.2f}".format
      (product_2_name, product_2_weight_g, product_2_weight_kg, product_2_cost, product_2_unit_price))

print("{}:  Weight: {} grams    Weight: {:.3f} kilograms    Cost: ${:.2f}   Unit Price: ${:.2f}".format
      (product_3_name, product_3_weight_g, product_3_weight_kg, product_3_cost, product_3_unit_price))

print("{}:  Weight: {} grams    Weight: {:.3f} kilograms    Cost: ${:.2f}   Unit Price: ${:.2f}".format
      (product_4_name, product_4_weight_g, product_4_weight_kg, product_4_cost, product_4_unit_price))

print("{}:  Weight: {} grams    Weight: {:.3f} kilograms    Cost: ${:.2f}   Unit Price: ${:.2f}".format
      (product_5_name, product_5_weight_g, product_5_weight_kg, product_5_cost, product_5_unit_price))

print("{}:  Weight: {} grams    Weight: {:.3f} kilograms    Cost: ${:.2f}   Unit Price: ${:.2f}".format
      (product_6_name, product_6_weight_g, product_6_weight_kg, product_6_cost, product_6_unit_price))

# So the output looks nice
print()

# Recommendations (header text)
print(" *** RECOMMENDATIONS *** ")

# So the output looks nice
print()

# Printing the users budget to remind them
print("Your budget is: ${:.2f}".format(budget))

# So the output looks nice
print()

# If the product (1) is less than or equal to budget print the below statement
if product_1_unit_price <= budget:
    print("{}:      Cost: ${:.2f}       Unit Price: ${:.2f}".format
          (product_1_name, product_1_cost, product_1_unit_price))

# If the product (2) is less than or equal to budget print the below statement
if product_2_unit_price <= budget:
    print("{}:      Cost: ${:.2f}       Unit Price: ${:.2f}".format
          (product_2_name, product_2_cost, product_2_unit_price))

# If the product (3) is less than or equal to budget print the below statement
if product_3_unit_price <= budget:
    print("{}:      Cost: ${:.2f}       Unit Price: ${:.2f}".format
          (product_3_name, product_3_cost, product_3_unit_price))

# If the product (4) is less than or equal to budget print the below statement
if product_4_unit_price <= budget:
    print("{}:      Cost: ${:.2f}       Unit Price: ${:.2f}".format
          (product_4_name, product_4_cost, product_4_unit_price))

# If the product (5) is less than or equal to budget print the below statement
if product_5_unit_price <= budget:
    print("{}:      Cost: ${:.2f}       Unit Price: ${:.2f}".format
          (product_5_name, product_5_cost, product_5_unit_price))

# If the product (6) is less than or equal to budget print the below statement
if product_6_unit_price <= budget:
    print("{}:      Cost: ${:.2f}       Unit Price: ${:.2f}".format
          (product_6_name, product_6_cost, product_6_unit_price))

# Lists of all of the users inputted data

# Product Names List
product_names = [product_1_name, product_2_name, product_3_name, product_4_name, product_5_name, product_6_name]

# Product Weights in grams lists
products_weights_g = [product_1_weight_g, product_2_weight_g, product_3_weight_g, product_4_weight_g,
                      product_5_weight_g, product_6_weight_g]

# Product Costs List
products_costs = [product_1_cost, product_2_cost, product_3_cost, product_4_cost, product_5_cost, product_6_cost]

# Lists of all of the computer generated data

# Products Weights in kilograms LIst
products_weights_kg = [product_1_weight_kg, product_2_weight_kg, product_3_weight_kg, product_4_weight_kg,
                       product_5_weight_kg, product_6_weight_kg]

# Products Unit Prices List
products_unit_prices = [product_1_unit_price, product_2_unit_price, product_3_unit_price, product_4_unit_price,
                        product_5_unit_price, product_6_unit_price]

# List of all of the other lists (Major_List)
Major_List = [product_names, products_weights_g, products_costs, products_weights_kg, products_unit_prices]


# To make the output look nice
print()
