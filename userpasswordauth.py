userinfo = {}
print("Do you want to sign up?")
i = str(input("Answer with a yes or no: "))
i = i.lower()
if i == 'yes':
    userinfo['user'] = str(input("Alrighty. What do you want your username to be: "))
    userinfo['passw'] = str(input("Cool! What do you want your password to be: "))
    print("Alrighty! Gotcha!")
    userinp = str(input("Please enter your username: "))
    userpassw = str(input("Please enter your password: "))
    if userinp == userinfo['user'] and userpassw == userinfo['passw']:
        print("Access granted!")
        
    else:
        print("Username or password is incorrect!")
        
else:
    print("Session closing...")