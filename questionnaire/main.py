while True:

    print ("Здравствуйте! \nПредлагаю Вам пройти небольшой тест. \nЭто не займет много времени. \nИтак начнем ")

    name = input("Введите имя: ")
    sex = input("Укажите Ваш пол (м \ ж): ")
    age = int(input("Введите Ваш возраст: "))
    if age <= 18:
        print f"Привет, {name}" 
    else:
        print f"Здравствуйте, {name}" 

    userAnswer = input("Какой Ваш любимый язык программирования:\n 1) Python \n 2) JavaScript \n 3) C# \n 4)Свой вариант(написать)\n")
    #на текстовые данные нужно ставить двойное равно в if'e - запомнить.
    # На несколько вариантов ответов используем "in"
    if userAnswer in ("1", "2", "3"):
       # print(string.lower)
        print f"Хороший выбор, {name}. Этот язык позволит Вам кодить для души, но также у Вас есть возможность получать неплохие деньги.\n Удачи в изучении. "
    else:
        print("Понятно. Но мы думаем, что Вам понравятся языки из нашей предложки")
    exitProgram = input("Чтобы выйти, введите q\nЧтобы продолжить, нажмите Enter: ")
    if exitProgram == "q":
        break



