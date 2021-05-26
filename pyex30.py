results = []
while True:
    print("Player 1, what do you choose?")
    p1 = int(input("\nPress 1 for: Rock,\nPress 2 for:  paper,\nPress 3 for:  scissor: "))
    print("Player 2, what do you choose?")
    p2 = int(input("\nPress 1 for: Rock,\nPress 2 for:  paper,\nPress 3 for:  scissor: "))
    
    #both choose same
    if p1 == 1 and p2 == 1:
        print("Both choose rock! Both are equal and nobody wins!")
        results.append('Draw')
    elif p1 == 2 and p2 == 2:
        print("Both choose Paper! Both are equal and nobody wins!")
        results.append('Draw')
    elif p1 == 3 and p2 == 3:
        print("Both choose scissor! Both are equal and nobody wins!")
        results.append('Draw')
    
    # player 1 chooses rock and wins all
    elif p1 == 1 and p2 == 2:
        print("Player 1 choose rock and Player 2 choose paper! Paper encloses the rock and Player 2 wins!")
        results.append('Player 1')
    elif p1 == 1 and p2 == 3:
        print("Player 1 choose rock and Player 2 choose scissor! The scissor cant cut the rock and Player 1 wins!")
        results.append('Player 1')
    
    #player 2 chooses rock
    elif p1 == 2 and p2 == 1:
        print("Player 1 choose paper and Player 2 choose rock! Paper encloses the rock and Player 1 wins!")
        results.append('Player 2')
    elif p1 == 3 and p2 == 1:
        print("Player 1 choose scissor and Player 2 choose rock! The scissor cant cut the rock and Player 2 wins!")
        results.append('Player 2')
    
    #player 1 chooses paper
    elif p1 == 2 and p2 == 1:
        print("Player 1 choose paper and Player 2 choose rock! Paper encloses the rock and Player 1 wins!")
        results.append('Player 2')
    elif p1 == 2 and p2 == 3:
        print("Player 1 choose paper and Player 2 choose scissors! The scissor cuts the paper and Player 2 wins!")
        results.append('Player 2')
    
    #player 2 chooses paper
    elif p1 == 1 and p2 == 2:
        print("Player 1 choose paper and Player 2 choose rock! Paper encloses the rock and Player 1 wins!")
        results.append('Player 1')
    elif p1 == 3 and p2 == 2:
        print("Player 1 choose scissors and Player 2 choose paper! The scissor cuts the paper and Player 1 wins!")
        results.append('Player 1')
    
    #player 1 chooses scissor
    elif p1 == 3 and p2 == 1:
        print("Player 1 choose scissors and Player 2 choose rock! Rock smashes appart the scissor and Player 2 wins!")
        results.append('Player 2')
    elif p1 == 3 and p2 == 2:
        print("Player 1 choose scissors and Player 2 choose paper! The scissor cuts the paper and Player 1 wins!")
        results.append('Player 1')
    
    #player 2 chooses scissor
    elif p1 == 1 and p2 == 3:
        print("Player 1 choose rock and Player 2 choose paper! Rock rips appart the paper and Player 1 wins!")
        results.append('Player 1')
    elif p1 == 2 and p2 == 3:
        print("Player 1 choose paper and Player 2 choose scissors! The scissor cuts the paper and Player 2 wins!")
        results.append('Player 2')
        
    gameover = str(input("Game over!\nWould you like to try again?\n[Y/N]: "))
    
    if gameover == 'N' or gameover == 'NO' or gameover == 'No' or gameover == 'nO' or gameover == 'no':
        print("Printing results...")
        print(results)
        print("Thanks for playing!")
        break
    
# Created by HyprClock.inc
# Connect on Discord: Rudemagician#8089
# Thanks for playing!