
def intcheck(question, low, high):
    valid = False
    while not valid:
        error = "Please enter you budget again".format(low, high)
        try:
            response = int(input("Enter you budget (e.g 15)? $"))
            if 1<= response <= 1000:
                 return response
            else:
                 print(error)
                 print()

        except ValueError:
            print(error)

        # Make the code recyclable

# main routine goes here
budget = intcheck ("Enter you budget (e.g 15)? ",1, 1000)
print("Your budget is: ${:.2f}".format(budget))

budget = float(input("What is your budget? (e.g. 15.60)? $"))
check_float = isinstance(budget, float)


if check_float == True:
    print("Your budget is: ${:.2f}".format(budget))

else:
    print("Please enter your budget again ({} input)".format(check_float))
    budget = input("What is your budget? ")
    print("Your budget is: {:.2f} dollars".format(budget))

    check_float = isinstance(budget, float)
    print(check_float)


budget_list = [budget]
