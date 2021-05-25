print("Hello there! Welcome to Supreme® California! What is your name?")
name = str(input())

print("Nice to meet you " + name + "!")

print("\nHere are our available tees for today:\n")
tees = ['Type 1 for: Supreme Box Logo', 'Type 2 for: Supreme Makai Gold', 'Type 3 for: Supreme Power Blue', 'Type 4 for: Supreme x LV', 'Type 5 for: Supreme Makasuka']

for shirts in tees:
    print(shirts)
print("\nWhat is your choice?")
selected = []
select = str(input())

if select == "1":
    print("Supreme Box Logo has been added!")
    selected.append('Supreme Box Logo')
elif select == "2":
    print("Supreme Makai Gold has been added!")
    selected.append('Supreme Makai Gold')
elif select == "3":
    print("Supreme Power Blue has been added!")
    selected.append('Supreme Power Blue')
elif select == "4":
    print("Supreme x LV has been added!")   
    selected.append('Supreme x LV')
elif select == "5":
    print("Supreme Makasuka has been added!")
    selected.append('Supreme Makasuka')

if selected:
    print("\nHere are your items:")
    print(selected)
else:
    print("Do you want to exit?")
    
SBL = "$175"
SMG = "$215"
SPB = "$444"
SXL = "$850"
SMA = "$1025"

if 'Supreme Box Logo' in selected:
    print("\nThe total bill is " + SBL + ".")
    
elif 'Supreme Makai Gold' in selected:
    print("\nThe total bill is " + SMG + ".")
    
elif 'Supreme Power Blue' in selected:
    print("\nThe total bill is " + SPB + ".")
    
elif 'Supreme x LV' in selected:
    print("\nThe total bill is " + SXL + ".")
    
elif 'Supreme Makasuka' in selected:
    print("\nThe total bill is " + SMA + ".")
    
print("Thanks for shopping with us!\nHope to see you soon :D")
