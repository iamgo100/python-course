def squareSequenceDigit(n):
    num = 0
    sequence = ''
    while len(sequence) <= n:
        num += 1
        sequence += str(num*num)
    if len(sequence) == n:
        return int(sequence) % 10
    else:
        l = len(sequence) - n
        num1 = int(sequence) // 10**l
        return num1 % 10

if __name__ == "__main__":
    assert squareSequenceDigit(1) == 1, "предполагаемый результат: 1"

    assert squareSequenceDigit(2) == 4, "предполагаемый результат: 4"

    assert squareSequenceDigit(7) == 5, "предполагаемый результат: 5"
    
    assert squareSequenceDigit(8) == 3, "предполагаемый результат: 3"

    assert squareSequenceDigit(12) == 6, "предполагаемый результат: 6"

    assert squareSequenceDigit(17) == 0, "предполагаемый результат: 0"

    assert squareSequenceDigit(27) == 9, "предполагаемый результат: 9"
    
    print('Все тесты пройдены успешно')