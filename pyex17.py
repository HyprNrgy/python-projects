missipi = {
    'm':1,
    'i':4,
    's':4,
    'p':2,
}

print("In the word 'Mississippi:")
for word, number in sorted(missipi.items()):
    print("\tThe letter " + word + " occured " + str(number) + " times")