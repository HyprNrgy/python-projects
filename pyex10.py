print("Hello there! What is your salary?")
salary = int(input())
print("What is your working experience?")
wex = int(input())

if wex >= 5:
    print("You will be given a bonus!")
    bonus = salary*5/100
    total = bonus + salary
    print("Here is your total salary: " + str(total))

else:
    print("Since your working experience is lower than 5, your salary is: " + str(salary))