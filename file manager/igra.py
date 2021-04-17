import random


def game():
    number = random.randint(1, 100)
    print('Компьютер загадал число од 1 до 100. ты должен его угадать')
    user_number = int(input("Введи число "))
    while True:
        if number == user_number:
            print("Вы угадали")
            break
        elif number > user_number:
            print("Число должно быть больше")
            user_number = int(input("Введи число "))
        else:
            print("Число должно быть меньше")
            user_number = int(input("Введи число "))
