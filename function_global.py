x=50

def func():
    global x
    print('x is ', x)
    x=2
    print('changed global x is', x)
func()
print('Vaule of x is', x)