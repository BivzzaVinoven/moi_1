from decouple import config
from random import choice
def start():

    money = int(config('MY_MONEY'))

    print(money)

    ist = range(1, 31)

    print(ist)

    while True:
        number = int(input('Введите число от 1 до 30: '))

        bet = input('Введите вашу ставку: ')
        while True:
            if type(bet) != int:
                bet = input(f"Вводите целое число меньшее {money}: ")
            if bet.isdigit() and int(bet) <= money:
                bet = int(bet)
                break


        win = choice(ist)

        if number == win:
            money += bet * 2
            print(f"Вы выйграли {bet*2}$")

        else:
            money -= bet
            print(f"Вы проиграли  {bet}$")

        print(f"Ваш текущий балан: {money}")

        command = input('хотите продолжить игру ?\n1)да\n2)нет\n ')

        if command.lower() == 'нет':
            break

