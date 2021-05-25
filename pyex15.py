opp = {
    'left':'right',
    'right':'left',
    'top':'bottom',
    'bottom':'top'
    }

print("Tell me any side, left, right, top or bottom: ")
i = str(input().lower())

if i == 'left':
    print(opp['left'])
        
if i == 'right':
    print(opp['right'])
        
if i == 'top':
    print(opp['top'])
        
if i == 'bottom':
    print(opp['bottom'])