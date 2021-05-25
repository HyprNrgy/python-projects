range_num = range(1,100)
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number you want the previous number to be divided by: "))
if num1 % num2 == 0:
    print(str(num1) + " is divisible by " + str(num2) + "!!")
else:
    print(str(num1) + " is not divisible by " + str(num2) + "!!")