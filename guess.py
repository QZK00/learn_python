number = 55
guess = int(input('enter an integer : '))

if guess == number:
    print('congratulations,you guessed it')
    print('but you not win any prizes')
elif guess<number:
    print(' too small')
else:
    print('too higher')

print('done')

print('the number is {}'.format(55))
