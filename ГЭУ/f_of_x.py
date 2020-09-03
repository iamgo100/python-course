x=float(input('Введите х: '))

def f(x):
    if -2.4<=x<=5.7:
        return x**2
    else:
        return 4

print('Значение функции равно',f(x))
