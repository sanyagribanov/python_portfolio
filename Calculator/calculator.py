while True:
    a = int(input("Введите 1-е число: "))
    b = int(input("Введите 2-е число: "))
    res = input("Выберите действие: \n1 - сложение; \n2 - вычитание; \n3 - умножение; \n4 - деление.\n")
    def multi_num(res):
        if res == '1':
            return a + b
        if res == '2':
            return a - b
        if res == '3':
            return a * b
        if res == '4':
            return a / b
        raise ValueError('Неизвестный оператор {}'.format.res)
    print(multi_num(res))
    exit = input("Введите q, чтобы выйти. \nНажмите Enter, чтобы продолжить использовать Калькулятор: ")
    if exit == "q":
        break
    
    

    