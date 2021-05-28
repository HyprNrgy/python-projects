import time
from time import sleep

num = 1
userdetails = {}
rooms = {
    'Standard' : '$85 Per Night (incl of Taxes)',
    'Premium' : '$125 Per Night (incl of Taxes)',
    'Supreme' : '$185 Per Night (incl of Taxes)',
    'Jr. Suite' : '$250 Per Night (incl of Taxes)',
    'Sr. Suite' : '$325 Per Night (incl of Taxes)',
    'Penthouse' : '$555 Per Night (incl of Taxes)'
}

print("\nWelcome to Hilton Hotels Canada!")
sleep(2)
fn = input("May I get your first name please: ")
sleep(1.5)
ln = input("May I get your last name please: ")
sleep(1.5)
while True:
    try:
        gen = int(input("\nWhat if your gender?\nPress[1] for Male\nPress[2] for Female: "))
        sleep(1)
        break
    except ValueError:
        print("Sorry, thats an invalid option!\nTry again")

def details_greet(first,last,gender):
    if gender == 1:
        print("\nNice to meet you Mr. " + first + ' ' + last + "!")
        sleep(1.25)
        print("I shall be right back!")
        userdetails['name'] = first
    else:
        print("\nNice to meet you Mrs. " + first + ' ' + last + "!")
        sleep(1.25)
        print("I shall be right back!")
        userdetails['name'] = first
    return

details_greet(first = fn, last = ln,gender = gen)

print("\nWe have the following rooms available: ")
sleep(1.75)
for room,details in rooms.items():
    print("\n" + str(num) + ": " + room + " costs " + details + ".")
    sleep(1.5)
    num += 1
    
while True:
    try:
        choice = int(input("\nPlease enter the number of the room you would like to book: "))
        sleep(1.25)
        break
    except ValueError:
        print("Invalid selection!\nTry again!")
        
print("Alright!")
sleep(1.25)
while True:
    try:
        duration = int(input("\nPlease enter duration of your stay (number of nights): "))
        sleep(1.25)
        break
    except ValueError:
        print("Something went wrong!\nTry again!")
sleep(1.25)

if choice == 1:
    cost = duration*85
    sleep(1.25)
    print("\nThe total cost for the Standard room for " + str(duration) + " nights will be " + str(cost) + " USD")
    userdetails['cost'] = cost
    
elif choice == 2:
    cost = duration*125
    sleep(1.25)
    print("\nThe total cost for the Premium room for " + str(duration) + " nights will be " + str(cost) + " USD")
    userdetails['cost'] = cost
    
elif choice == 3:
    cost = duration*185
    sleep(1.25)
    print("\nThe total cost for the Supreme room for " + str(duration) + " nights will be " + str(cost) + " USD")
    userdetails['cost'] = cost
    
elif choice == 4:
    cost = duration*250
    sleep(1.25)
    print("\nThe total cost for the Jr. Suite for " + str(duration) + " nights will be " + str(cost) + " USD")
    userdetails['cost'] = cost
    
elif choice == 5:
    cost = duration*325
    sleep(1.25)
    print("\nThe total cost for the Sr. Suite for " + str(duration) + " nights will be " + str(cost) + " USD")
    userdetails['cost'] = cost
    
elif choice == 6:
    cost = duration*555
    sleep(1.25)
    print("\nThe total cost for the Penthouse for " + str(duration) + " nights will be " + str(cost) + " USD")
    userdetails['cost'] = cost
   
   
print("\nHere are your final details:")
sleep(2)
#for key,value in userdetails.items():
print("\tYour name is " + userdetails['name'] + ".")
sleep(1)
print("\tYour final bill is " + str(userdetails['cost']) + " USD (incl of taxes).")
sleep(1)
print("\nThanks for booking! Stay safe!\n") 