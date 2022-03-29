import random

choice = random.randint(1, 20)
tries = 5
punctire = "---------------------------------------"
while True:
    print(f"Количество попыток {tries}")
    userAnswer = int(input("Введите число от 1 до 20: "))
    if userAnswer > choice:
        print(f"Это слишком большое число. Напишите число поменьше\n{punctire}")
        tries -= 1
    elif userAnswer < choice:
        print(f"Это слишком маленькое число. Напишите число побольше\n{punctire}")
        tries -= 1
    elif userAnswer == choice:
        print(f"Поздравляю, вы угадали. Это число {choice}")
        break
    if tries == 0:
        print("Попытки кончились, вы проиграли")
        break
input("Нажмите Enter для выхода...")

