print("Whats your quantity?")
qty = int(input())
unit = 100

total = qty*unit

if total >= 1000:
    print("You will be getting a discount!")
    amount = 10/100*total
    amounts = total - amount
    print("The discounted amount is: " + str(amount))
    print("And the total is " + str(amounts))

else:
    print("The total amount is " + str(total))