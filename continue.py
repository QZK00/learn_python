while True:
    s = input('Enter something :')
    if s=='quit':
        break
    elif len(s)<3:
        print('too small')
        continue
    print('Input is  of sufficient length')