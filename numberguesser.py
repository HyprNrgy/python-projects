# Minor bug fixes as of 27.05.2021
# Known bugs: Input control needed + restart of 2 loops
# Made by Kuldeep R
# Enjoy :D!!
import random
while True:
    a = random.randint(1,9)
    #print(a) #<--- un-comment the following line of code for testing purposes only!!!
    break

while True:
    print("\nPython has a number in mind.\nPython says the number is between 0 and 10!")
    g1 = int(input("\nWhat number could it be?\nEnter your guess: "))

    if g1 == a:
        print("Nailed it!")
        break
        #again = input("Wanna try again? ")
        #if again == 'N' or again == 'n' or again == 'NO' or again == 'no' or again == 'No' or again == 'nO':
            #break
        #The above lines of code are under review/testing as of 27.05.2021
        
    elif g1 == a+1:
        print("\nA bit high")
    
    elif g1 == a-1:
        print("\nA bit low")
    
    elif g1 == a+2:
        print("\nA little too high")
        
    elif g1 == a-2:
        print("\nA little too low")
        
    elif g1 == a+3:
        print("\nQuite high!")
        
    elif g1 == a-3:
        print("\nQuite low!")
        
    elif g1 == a+4:
        print("\nHigh!!")
        
    elif g1 == a-4:
        print("\nLow!!")
        
    elif g1 == a+5:
        print("\nToo high!!!")
        
    elif g1 == a-5:
        print("\nToo low!!!")
        
    elif g1>a+5:
        print("\nToo High!!!")
        
    elif g1<a-5:
        print("\nToo low!!!")
        
print("\nThanks for playing! Hope you enjoyed it!")