def float_check(choice, options):
    for var_list in options:
        if choice in var_list:
            chosen = var_list[0]
            is_valid = float
            break

        else:
            is_valid = "error"

    if is_valid == float:
        return chosen
    else:
        print("Please enter a number")
        print()
        return "invalid choice"


yes_no = float

check_budget = "invalid choice"
while check_budget == "invalid choice":
    ask_budget = input("What is you budget? (e.g. $50.20)? ")
    check_budget = float_check(ask_budget, yes_no)







