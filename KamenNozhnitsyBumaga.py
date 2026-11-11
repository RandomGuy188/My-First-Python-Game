import random
import os

HelloWorld = 1

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

B = ["Камень", "Ножницы", "Бумага"]

if HelloWorld == 1:
    A = input(f"Добро пожаловать в мини-игру: Камень-Ножницы-Бумага, выберите 0 чтобы начать игру: " )

while True:
    if A == "0":
        clear_console()
        D = input(f"Камень-Ножницы-Бумага, Цу-Е-Фа: 1 - Камень; 2 - Ножницы; 3 - Бумага: ")
        C = random.choice(B)
    else:
        clear_console()
        A = input("Неправильный ввод символа, повторите попытку: ")
        continue
    
    if D == "1":
        E = "Камень"
    elif D == "2":
        E = "Ножницы"
    elif D == "3":
        E = "Бумага"
    else:
        clear_console()
        input("Неправильный ввод символа, повторите попытку: ")
        continue
    
    if E == C:
        clear_console()
        print(f"Эх, Ничья! Бот как и вы выбрал {C}")
        input("Выберите любой символ чтобы продолжить: ")
    elif D == "1" and C == "Ножницы":
        clear_console()
        print(f"Победа! Бот выбрал: {C}")
        input("Выберите любой символ чтобы продолжить: ")
    elif D == "2" and C == "Камень":
        clear_console()
        print(f"Поражение! Бот выбрал: {C}")
        input("Выберите любой символ чтобы продолжить: ")
    elif D == "2" and C == "Бумага":
        clear_console()
        print(f"Победа! Бот выбрал: {C}")
        input("Выберите любой символ чтобы продолжить: ")
    elif D == "3" and C == "Ножницы":
        clear_console()
        print(f"Поражение! Бот выбрал: {C}")
        input("Выберите любой символ чтобы продолжить: ")
    elif D == "3" and C == "Камень":
        clear_console()
        print(f"Победа! Бот выбрал: {C}")
        input("Выберите любой символ чтобы продолжить: ")
    elif D == "1" and C == "Бумага":
        clear_console()
        print(f"Поражение! Бот выбрал: {C}")
        input("Выберите любой символ чтобы продолжить: ")