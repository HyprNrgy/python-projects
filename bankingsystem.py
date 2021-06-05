import time
from time import sleep

user_0 = {}
bank = {'amount':0,
        'Loan':'None'
        }

def signup():
        sleep(0.5)
        print("\nAlright! We shall create a new account for you!")
        sleep(1.5)
        name = input("What is your first name: ")
        print("\nNice too meet you " + name + "!")
        user_0['first'] = name.title()
        sleep(1.5)
        last = input("What is your last name: ")
        print("\nGotcha!")
        user_0['last'] = last.title()
        sleep(1.5)
        age = int(input("Whats your age: "))
        print("\nNever too young to open a new account!")
        user_0['age'] = age
        while True:
            sleep(1.5)
            bnumber = input("Please enter your desired alpha-numeric bank number thats 8 digits long: ")
            if len(bnumber) == 8:
                sleep(0.5)
                print("\nYour bank number works fine!")
                user_0['bnumber'] = str(bnumber)
                break
            else:
                sleep(0.5)
                print("\nSorry, your bank number is either too short or long!")
        while True:
            sleep(1.5)
            passw = input("Please enter a password: ")
            repassw = input("Please re-enter your password: ")
            if len(passw) in range(0,3):
                print("\nWell, your password is too weak!")
            if len(passw) in range(3,6):
                print("\nWell, your password is weak!")
            if len(passw) in range(6,9):
                print("\nWell, your password is okay!")
            if len(passw) in range(9,11):
                print("\nWell, your password is good!")
            if len(passw) in range(11,14):
                print("\nWell, your password is great!")
            if len(passw) in range(14,17):
                print("\nWell, your password is strong!")
            if len(passw) in range(17,22):
                print("\nWell, your password is super-strong💪!")
            if passw == repassw:
                print("And, the passwords match!")
                user_0['password'] = passw
                break
            else:
                    print("\nThe passwords don't match!\nTry again!")
        return
        

def login(user_data):
    sleep(0.5)
    usr= input("\nBank number\n>>> ")
    sleep(0.5)
    passwrd = input("Password\n>>> ")
    while True:
        if usr == user_data['bnumber'] and passwrd == user_data['password']:
            sleep(1)
            print("\nAccess granted " + user_data['first'] + "!\nHave a nice day!")
            break
        else:
            sleep(0.5)
            print("Access denied!\nTry again!")
    return


def withdraw(bank):
    sleep(0.5)
    while bank['amount'] > 0:
        print("\nYou have " + str(bank['amount']) + ".\nHow much would you like to withdraw?")
        withdrw = int(input(">>> "))
        if withdrw > bank['amount']:
            sleep(0.5)
            print("Sorry! You only have " + str(bank['amount']) + "!!\n Try again")
        if withdrw <= bank['amount']:
            print("\nWithdrawing " + str(withdrw) + "...")
            bank['amount'] -= withdrw
            sleep(1.5)
            print("\nDone!\nYou have " + str(bank['amount']) + ".")
            break
    return


def deposit(bank):
    sleep(0.5)
    print("\nYou currently have " + str(bank['amount']) + "!\nHow much would you like to deposit?")
    dep = int(input(">>> "))
    bank['amount'] = dep
    sleep(1.5)
    print("\nDone!\nYou now have " + str(bank['amount']) + ".")
    return


def loan(bank):
    sleep(0.5)
    print("\nYou currently have " + str(bank['amount']) + ".")
    print("Please enter the amount of your desired loan")
    req = int(input(">>> "))
    amt = (5/100)*req
    print("\nSo you requested a loan of " + str(req) + ".\nAfter 5 percent of interest, you will have to pay " + str(amt) + " per month.")
    bank['Loan'] = req


def update(user_0):
    sleep(0.5)
    while True:
        print("\nWhich part of your profile would you like to update?\nPress[1] to update your 'First Name'\nPress[2] to update your 'Last Name'\nPress[3] to update your 'age'\nPress[4] to update your 'Bank Number'\nPress[5] to update your 'Password'\nPress[6] when done!")
        inp = int(input(">>> "))
        
        if inp == 1:
            sleep(0.5)
            print("Please enter your new 'First Name'")
            fn = input(">>> ")
            user_0['first'] = fn.title()
            sleep(0.5)
            print("Your first name has been updated!")
            
        if inp == 2:
            sleep(0.5)
            print("Please enter your new 'Last Name'")
            ln = input(">>> ")
            user_0['last'] = ln.title()
            sleep(0.5)
            print("Your last name has been updated!")
            
        if inp == 3:
            sleep(0.5)
            print("Please enter your new 'Age'")
            ag = int(input(">>> "))
            user_0['age'] = ag
            sleep(0.5)
            print("Your age has been updated!")
            
        if inp == 4:
            sleep(0.5)
            print("Please enter your new alpha-numeric 'Bank Number'")
            nbn = input(">>> ")
            user_0['bnumber'] = nbn
            sleep(0.5)
            print("Your bank number has been updated!")
            
        if inp == 5:
            sleep(0.5)
            print("Please enter your new 'Password'")
            pss = input(">>> ")
            print("Please re-enter your new 'Password'")
            rpss = input(">>> ")
            if pss == rpss:
                sleep(0.5)
                print("\nYour password has been changed successfully!")
                user_0['password'] = str(pss)
            else:
                sleep(0.5)
                print("\nSorry, your passwords don't match!\nTry again later!")
                
        if inp == 6:
            print("Saving...")
            sleep(0.5)
            break

while True:
    #The database where all data is stored is in user_0
    print("\n\nHello and welcome to Le Bank!")

    sleep(1.5)
    
    print("\nWhat would you like to do today: ")

    while True:
        try:
            main = int(input("\nPress [1] to sign up\nPress [2] to login\n>>> "))
            break
        except ValueError:
            sleep(1.5)
            print("\nWoah! Thats not a vaild option!\nTry again!")

        
    #signup = main1()
    if main == 1:
        signup()
        sleep(0.5)
        print("\nFinishing creating your bank account...")
        sleep(3)
        
    if main == 2:
        login(user_0)
        break
    
print("\nGood day " + user_0['first'].title() + "!")

while True:
    sleep(1.5)
    print("\nWhat would you like to do today:\n\nPress [1] to 'Withdraw Cash'\nPress [2] to 'Deposit Cash'\nPress [3] to 'Apply For A Loan'\nPress [4] to 'Update User Data'\nPress [5] to 'Quit'")
    todo = int(input(">>> "))    
    
    if todo == 1:
        withdraw(bank)
        
    if todo == 2:
        deposit(bank)
            
    if todo == 3:
        loan(bank)
            
    if todo == 4:
        update(user_0)
    
    if todo == 5:
        print("Quitting...")
        sleep(2.5)
        print("\Have a nice day " + user_0['first'].title() + "!")
        sleep(0.25)
        break