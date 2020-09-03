value=input('Введите pH: ')

if len(value)>0:
    pH=float(value)
    if pH==7.0:
        print(pH,'Water')
    elif 7.36<pH<7.44:
        print(ph,'Blood')
    else:
        print('What\'s it?')
else:
    print('Введите значение pH!')
