room=input('Выберете зал:\nКрасный - фильм \"Пятница\"\nСиний - фильм \"Чемпионы: Быстрее. Выше. Сильнее\"\nГолубой - фильм \"Пернатая банда\"\n')
time=input('Введитете время сеанса: ')
amt=int(input('Введите количество билетов: '))

if room=='Красный' or room=='красный':
    if time=='12 часов' or time=='12:00' or time=='12':
        if 5<amt<=10:
            cost=250*95/100*amt
            print('К оплате:',cost,'рублей')
        elif amt>10:
            cost=250*90/100*amt
            print('К оплате:',cost,'рублей')
        else:
            cost=250*amt
            print('К оплате:',cost,'рублей')
    elif time=='16 часов' or time=='16:00' or time=='16':
        if 5<amt<=10:
            cost=350*95/100*amt
            print('К оплате:',cost,'рублей')
        elif amt>10:
            cost=350*90/100*amt
            print('К оплате:',cost,'рублей')
        else:
            cost=350*amt
            print('К оплате:',cost,'рублей')
    elif time=='20 часов' or time=='20:00' or time=='20':
        if 5<amt<=10:
            cost=450*95/100*amt
            print('К оплате:',cost,'рублей')
        elif amt>10:
            cost=450*90/100*amt
            print('К оплате:',cost,'рублей')
        else:
            cost=450*amt
            print('К оплате:',cost,'рублей')
    else:
        print('В это время сеанса не найдено')
elif room=='Синий' or room=='синий':
    if time=='10 часов' or time=='10:00' or time=='10':
        if 5<amt<=10:
            cost=250*95/100*amt
            print('К оплате:',cost,'рублей')
        elif amt>10:
            cost=250*90/100*amt
            print('К оплате:',cost,'рублей')
        else:
            cost=250*amt
            print('К оплате:',cost,'рублей')
    elif time=='13 часов' or time=='13:00' or time=='13':
        if 5<amt<=10:
            cost=350*95/100*amt
            print('К оплате:',cost,'рублей')
        elif amt>10:
            cost=350*90/100*amt
            print('К оплате:',cost,'рублей')
        else:
            cost=350*amt
            print('К оплате:',cost,'рублей')
    elif time=='16 часов' or time=='16:00' or time=='16':
        if 5<amt<=10:
            cost=350*95/100*amt
            print('К оплате:',cost,'рублей')
        elif amt>10:
            cost=350*90/100*amt
            print('К оплате:',cost,'рублей')
        else:
            cost=350*amt
            print('К оплате:',cost,'рублей')
    else:
        print('В это время сеанса не найдено')
elif room=='Голубой' or room=='голубой':
    if time=='10 часов' or time=='10:00' or time=='10':
        if 5<amt<=10:
            cost=350*95/100*amt
            print('К оплате:',cost,'рублей')
        elif amt>10:
            cost=350*90/100*amt
            print('К оплате:',cost,'рублей')
        else:
            cost=350*amt
            print('К оплате:',cost,'рублей')
    elif time=='14 часов' or time=='14:00' or time=='14':
        if 5<amt<=10:
            cost=450*95/100*amt
            print('К оплате:',cost,'рублей')
        elif amt>10:
            cost=450*90/100*amt
            print('К оплате:',cost,'рублей')
        else:
            cost=450*amt
            print('К оплате:',cost,'рублей')
    elif time=='18 часов' or time=='18:00' or time=='18':
        if 5<amt<=10:
            cost=450*95/100*amt
            print('К оплате:',cost,'рублей')
        elif amt>10:
            cost=450*90/100*amt
            print('К оплате:',cost,'рублей')
        else:
            cost=450*amt
            print('К оплате:',cost,'рублей')
    else:
        print('В это время сеанса не найдено')
else:
    print('Такого зала не найдено. Проверьте написание зала и попробуйте еще раз')
input()