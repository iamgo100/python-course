x=int(input('Введите первое число: '))
y=int(input('Введите второе число: '))

def chi(x,y):
    if x>y:
        return x
    else:
        return y

print('Большее из чисел: ',chi(x,y))
    
