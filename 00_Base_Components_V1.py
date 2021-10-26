
# Functions
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Please enter you budget again".format(low, high)
        try:
            response = float(input("Enter you budget (e.g $15.60)? $"))
            if 1 <= response <= 1000:
                return response
            else:
                print(error)
                print()

        except ValueError:
            print(error)



# Calling the fuction and printing user feadback
budget = intcheck ("Enter you budget (e.g 15)? ",1, 1000)
print("Your budget is: ${:.2f}".format(budget))

# Lists
budget_list = [budget]


# Names of products
product_1_name = input("What is the name of this product? ").title()
product_2_name = input("What is the name of this product? ").title()
product_3_name = input("What is the name of this product? ").title()
product_4_name = input("What is the name of this product? ").title()
product_5_name = input("What is the name of this product? ").title()
product_6_name = input("What is the name of this product? ").title()


# Weights of products
product_1_weight_g = int(input("What is the weight of the {} in grams? ".format(product_1_name)))
product_2_weight_g = int(input("What is the weight of the {} in grams? ".format(product_2_name)))
product_3_weight_g = int(input("What is the weight of the {} in grams? ".format(product_3_name)))
product_4_weight_g = int(input("What is the weight of the {} in grams? ".format(product_4_name)))
product_5_weight_g = int(input("What is the weight of the {} in grams? ".format(product_5_name)))
product_6_weight_g = int(input("What is the weight of the {} in grams? ".format(product_6_name)))

# Converting the weight of the product in grams to kilograms
product_1_weight_kg = product_1_weight_g / 1000
product_2_weight_kg = product_2_weight_g / 1000
product_3_weight_kg = product_3_weight_g / 1000
product_4_weight_kg = product_4_weight_g / 1000
product_5_weight_kg = product_5_weight_g / 1000
product_6_weight_kg = product_6_weight_g / 1000

# Costs of the products
product_1_cost = input("What is the cost of {}? $".format(product_1_name))
product_2_cost = input("What is the cost of {}? $".format(product_2_name))
product_3_cost = input("What is the cost of {}? $".format(product_3_name))
product_4_cost = input("What is the cost of {}? $".format(product_4_name))
product_5_cost = input("What is the cost of {}? $".format(product_5_name))
product_6_cost = input("What is the cost of {}? $".format(product_6_name))

print()

# Printing out all of the inputted information and computer generated information in print stamens

print("{}:  Weight: {} grams    Weight: {} kilograms    Cost: ${}".format(product_1_name, product_1_weight_g,
                                                                          product_1_weight_kg, product_1_cost ))

print("{}:  Weight: {}  grams   Weight: {} kilograms    Cost: ${}".format(product_2_name, product_2_weight_g,
                                                                          product_2_weight_kg, product_2_cost))

print("{}:  Weight: {}  grams   Weight: {} kilograms    Cost: ${}".format(product_3_name, product_3_weight_g,
                                                                          product_3_weight_kg, product_3_cost))

print("{}:  Weight: {}  grams   Weight: {} kilograms    Cost: ${}".format(product_4_name, product_4_weight_g,
                                                                          product_4_weight_kg, product_4_cost))

print("{}:  Weight: {}  grams   Weight: {} kilograms    Cost: ${}".format(product_5_name, product_5_weight_g,
                                                                          product_5_weight_kg, product_5_cost))

print("{}:  Weight: {}  grams   Weight: {} kilograms    Cost: ${}".format(product_6_name, product_6_weight_g,
                                                                          product_6_weight_kg, product_6_cost))
