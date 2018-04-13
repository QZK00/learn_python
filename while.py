number = 23
running = True

while running:
    guess = int(input('enter an integer :'))
    if guess == number:
        print('congratulation , you guessed it')
        running = False
    elif guess < number:
        print('NO,It is little higher than that ')
    else:
        print('No,It is little lower than that')
else:
    print('ther while loop is over')

print('Done')
