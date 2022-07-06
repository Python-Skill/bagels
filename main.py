# create by Egoshin Alexey 07/2022
# encoding: UTF-8

from random import randint

# функция вывода информации об игре
def show_info():
    print(
        "Бейглз – дедуктивная логическая игра.",
        "Автор: Алексей Егошин alexegoshin0403@yandex.ru",
        "\nЯ загадал 3-значное число. Попробуйте угадать какое именно.",
        "Вот несколько подсказок:",
        "Когда я говорю:      Я имею ввиду:",
        "Pico                 Одна цифра верна, но находится не на своей позиции.",
        "Fermi                Одна цифра верна и находится на своей позиции.",
        "Bagles               Ни одна цифра не является правильной.",
        "\nУ Вас есть 10 попыток, чтобы угадать загаданное число!", sep="\n")


# функция генерации случайного 3-значного числа
def get_secret_number():
    number = str(randint(1, 9)) + str(randint(0, 9)) + str(randint(0, 9))
    return number


# функция проверки валидности ввода от пользователя
def input_check(value: str):
    correct_values = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    if len(value) != 3:
        return False

    for i in value:
        if i not in correct_values:
            return False

    if value[0] == '0':
        return False

    return True


# функция ответа программы подсказками
def get_hints(secret_number: str, value: str):
    hints = []

    for i in range(0, len(value)):
        if value[i] == secret_number[i]:
            hints.append("Fermi")
        elif value[i] in secret_number:
            hints.append("Pico")

    if len(hints) == 0:
        hints.append("Bagles")

    return hints


# главная функция, содержащая игровой цикл
def main():
    show_info()

    while True:
        attempt_counter = 1

        secret_number = get_secret_number()

        while attempt_counter < 11:
            print("\nПопытка #", attempt_counter)
            attempt = input("> ")

            if input_check(attempt):
                if attempt == secret_number:
                    print("Вы угадали!")
                    break
                else:
                    print(*get_hints(secret_number, attempt))
            else:
                print("Введено неверное значение, попытка провалена!")

            attempt_counter += 1

        if attempt_counter > 10:
            print("\nВы проиграли! Загаданное число -", secret_number)

        print("\nХотите сыграть снова? (да или нет)")
        key = input("> ")

        if key.lower() in ["да", "нет"]:
            if key.lower() == "да":
                continue
            else:
                print("Спасибо за игру!")
                break
        else:
            print("Введено неверное значение, завершение программы!")
            break


if __name__ == '__main__':
    main()
