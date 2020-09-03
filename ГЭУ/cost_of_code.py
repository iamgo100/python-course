code=int(input('Введите код города: '))
minutes=int(input('Введите длительность переговоров (в минутах): '))

if code==343:
    cst=15*minutes
    print('Стоимость переговоров:',cst,'рублей')
elif code==381:
    cst=18*minutes
    print('Стоимость переговоров:',cst,'рублей')
elif code==473:
    cst=13*minutes
    print('Стоимость переговоров:',cst,'рублей')
elif code==485:
    cst=11*minutes
    print('Стоимость переговоров:',cst,'рублей')
else:
    print('Города с такии кодом не найдено')
input()