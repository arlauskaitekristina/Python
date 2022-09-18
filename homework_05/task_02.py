# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

from random import randint

def input_dat(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def p_print(name, k, counter, candies):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter} конфет. Осталось на столе {candies} конфет.")

player_one = input("Введите имя первого игрока: ")
player_two = input("Введите имя второго игрока: ")
candies = 2021
hod = randint(0,2) 
if hod:
    print(f"Первый ходит {player_one}")
else:
    print(f"Первый ходит {player_two}")

counter_one = 0 
counter_two = 0

while candies > 28:
    if hod:
        k = input_dat(player_one)
        counter_one += k
        candies -= k
        hod = False
        p_print(player_one, k, counter_one, candies)
    else:
        k = input_dat(player_two)
        counter_two += k
        candies -= k
        hod = True
        p_print(player_two, k, counter_two, candies)

if hod:
    print(f"Выиграл {player_one}")
else:
    print(f"Выиграл {player_two}")