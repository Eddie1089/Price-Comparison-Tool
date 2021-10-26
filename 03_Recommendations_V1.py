
# Functions
def number_check(question, low, high):
    valid = False
    while not valid:
        error = "Please enter you budget again (Incorrect input)".format(low, high)
        try:
            response = float(input("Enter you budget (e.g $15.60)? $"))
            if 1 <= response <= 1000:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)


budget = number_check("Enter you budget (e.g 15)? ", 1, 1000)
print("Your budget is: ${:.2f}".format(budget))

# Lists
budget = [budget]


# Names of products
product_1_name = input("What is the name of this product? ").title()
product_2_name = input("What is the name of this product? ").title()
product_3_name = input("What is the name of this product? ").title()
product_4_name = input("What is the name of this product? ").title()
product_5_name = input("What is the name of this product? ").title()
product_6_name = input("What is the name of this product? ").title()


# Weights of products in Grams
product_1_weight_g = int(input("What is the weight of the {} in grams? ".format(product_1_name)))
product_2_weight_g = int(input("What is the weight of the {} in grams? ".format(product_2_name)))
product_3_weight_g = int(input("What is the weight of the {} in grams? ".format(product_3_name)))
product_4_weight_g = int(input("What is the weight of the {} in grams? ".format(product_4_name)))
product_5_weight_g = int(input("What is the weight of the {} in grams? ".format(product_5_name)))
product_6_weight_g = int(input("What is the weight of the {} in grams? ".format(product_6_name)))

# Product Weight in Kilograms
product_1_weight_kg = product_1_weight_g / 1000
product_2_weight_kg = product_2_weight_g / 1000
product_3_weight_kg = product_3_weight_g / 1000
product_4_weight_kg = product_4_weight_g / 1000
product_5_weight_kg = product_5_weight_g / 1000
product_6_weight_kg = product_6_weight_g / 1000

# Product Cost
product_1_cost = float(input("What is the cost of {}? $".format(product_1_name)))
product_2_cost = float(input("What is the cost of {}? $".format(product_2_name)))
product_3_cost = float(input("What is the cost of {}? $".format(product_3_name)))
product_4_cost = float(input("What is the cost of {}? $".format(product_4_name)))
product_5_cost = float(input("What is the cost of {}? $".format(product_5_name)))
product_6_cost = float(input("What is the cost of {}? $".format(product_6_name)))

# Unit Price
product_1_unit_price = product_1_cost / product_1_weight_kg
product_2_unit_price = product_2_cost / product_2_weight_kg
product_3_unit_price = product_3_cost / product_3_weight_kg
product_4_unit_price = product_4_cost / product_4_weight_kg
product_5_unit_price = product_5_cost / product_5_weight_kg
product_6_unit_price = product_6_cost / product_6_weight_kg

print()

# Print statements
print("{}:  Weight: {} grams    Weight: {:.3f} kilograms    Cost: ${:.2f}   Unit Price: ${:.3f}".format
      (product_1_name, product_1_weight_g, product_1_weight_kg, product_1_cost, product_1_unit_price))

print("{}:  Weight: {} grams    Weight: {:.3f} kilograms    Cost: ${:.2f}   Unit Price: ${:.3f}".format
      (product_2_name, product_2_weight_g, product_2_weight_kg, product_2_cost, product_2_unit_price))

print("{}:  Weight: {} grams    Weight: {:.3f} kilograms    Cost: ${:.2f}   Unit Price: ${:.3f}".format
      (product_3_name, product_3_weight_g, product_3_weight_kg, product_3_cost, product_3_unit_price))

print("{}:  Weight: {} grams    Weight: {:.3f} kilograms    Cost: ${:.2f}   Unit Price: ${:.3f}".format
      (product_4_name, product_4_weight_g, product_4_weight_kg, product_4_cost, product_4_unit_price))

print("{}:  Weight: {} grams    Weight: {:.3f} kilograms    Cost: ${:.2f}   Unit Price: ${:.3f}".format
      (product_5_name, product_5_weight_g, product_5_weight_kg, product_5_cost, product_5_unit_price))

print("{}:  Weight: {} grams    Weight: {:.3f} kilograms    Cost: ${:.2f}   Unit Price: ${:.3f}".format
      (product_6_name, product_6_weight_g, product_6_weight_kg, product_6_cost, product_6_unit_price))

print()

# Recommendations
print(" *** RECOMMENDATIONS *** ")

if






