
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




budget = intcheck ("Enter you budget (e.g 15)? ",1, 1000)
print("Your budget is: ${:.2f}".format(budget))

budget = [budget]









