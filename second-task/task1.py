# Напишите программу компьютерной игры "Угадай число", в которой компьютер генерирует случайное целое число от 1 до 15,
# а пользователь должен его угадать.
# После каждой неудачной попытки пользователя, программа должна сообщать ему о том, больше это число, или меньше
# загаданного, а в случае угадывания - поздравлять с выигрышем.
from random import randint


answer = randint(1, 15)

def inputNum():
    while True:
        try:
            num = int(input("Введите число от 1 до 15: "))
            if 0 < num <= 15:
                return num
            else:
                print("Некорректный ввод. Попробуйте снова.")
        except ValueError:
            print("Некорректный ввод. Введите целое число от 1 до 15.")


def attempt(answer, num):
    if num == answer:
        return True
    elif num < answer:
        print("Число должно быть больше")
        return False
    else:
        print("Число должно быть меньше")
        return False


def begin(answer):
    solved = False
    while not solved:
        num = inputNum()
        solved = attempt(answer, num)
    print("Поздравляем, Вы отгадали число!")


if __name__ == "__main__":
    begin(answer)

