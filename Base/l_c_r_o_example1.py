while True:
    initial_currency = input("money of what currency do you have(uah/usd/rub)")
    amount = float(input("how much money do you have?"))
    final_currency = input("what currency do you need?(uah/usd/rub)")
    if initial_currency == "rub" or final_currency == "rub":
        print("Fuck you")
    elif initial_currency == "uah" and final_currency == "usd":
        print("in dollars it is: ", amount/37, "$", sep='')
    elif initial_currency == "usd" and final_currency == "uah":
        print("in hryvnas it is: ", amount*37, "₴", sep='')
    else:
        print("sorry, we don't work with this currency")
