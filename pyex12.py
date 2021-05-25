print("Age 1")
age1 = int(input())
print("Age 2")
age2 = int(input())
print("Age 3")
age3 = int(input())

if age1 > age2 and age1 > age3:
    print(age1)

elif age2 > age1 and age2 > age3:
    print(age2)
    
elif age3 > age1 and age3 > age2:
    print(age3)
    
else:
    print(age1, age2, age3)