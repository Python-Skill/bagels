# create by Egoshin Alexey 07/2022
# encoding: UTF-8

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


def main():
    show_info()


if __name__ == '__main__':
    main()
