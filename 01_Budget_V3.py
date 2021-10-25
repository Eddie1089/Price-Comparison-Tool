budget = input("What is your budget? ")

check_float = isinstance(budget, float)

if check_float == True:
    print("Your budget is: {} dollars".format(budget))

else:
    print("Please enter your budget again ({} input)".format(check_float))
    budget = input("What is your budget? ")
    print("Your budget is: {} dollars".format(budget))

    check_float = isinstance(budget, float)
    print(check_float)


budget_list = [budget]







