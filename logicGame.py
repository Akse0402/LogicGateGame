"""Logic Gate Game - The game that will test your knowlegde on Logic gates"""

from numpy import random
from time import sleep

# Logic gates: NOT, AND, OR, NAND, NOR, XOR, XNOR
# TODO: Fix print statements
# TODO: Lav det i Pygame - Gør først dette når spillet er lavet her

# Settings
tableLenght = 5
table = []
tableGate = []
tableAnswer = []
tableCAnswer = []
gameModes = ["OR", "XOR", "AND", "NOT"]
gameMode = ""


def startGame(tableLenght, table, tableGate, gameModes, gameMode):
    print("Velkommen til Logic Gate Game!\n")
    while True:
        try:
            gameType = int(input("Vælg dit gamemode - (1:Or) (2:Xor) (3:And) (4:Nand): "))
            if 1 <= gameType <= 4:
                gameMode = gameModes[gameType - 1]
                print(f"Du valgte nr. {gameType} gamemode: {gameMode}\n")
                sleep(0.5)
                break
        except ValueError:
            print("Du skal vælge et tal mellem 1-4")

    # Generer tal til Tables
    for _ in range(tableLenght):
        table.append(random.randint(0, 2))
    for _ in range(tableLenght):
        tableGate.append(random.randint(0, 2))
    Game(gameType)


def Game(gameType):
    # OR gamemode
    if gameType == 1:
        tableCAnswer = [a | b for a, b in zip(table, tableGate)]
        print("Du har tabellerne:\n", table, "\n", tableGate, "\n")
        print(f"Du skal hermed nedskrive {gameMode} operationen for de 2 tabeller")
        i = 0
        while len(tableAnswer) < tableLenght:
            try:
                tableAns = int(input(f"Angiv {gameMode} operation for {table[i]} - "
                                    f"{tableGate[i]}: "))
                if 0 <= tableAns <= 1:
                    tableAnswer.append(tableAns)
                    print("Svar:", tableAnswer)
                    i += 1
                else:
                    print("Tallet skal være et binært tal")
            except ValueError:
                print("Det skal være et tal")

    # XOR gamemode
    if gameType == 2:
        tableCAnswer = [a ^ b for a, b in zip(table, tableGate)]
        print("Du har tabellerne:\n", table, "\n", tableGate, "\n")
        print(f"Du skal hermed nedskrive {gameMode} operationen for de 2 tabeller")
        i = 0
        while len(tableAnswer) < tableLenght:
            try:
                tableAns = int(input(f"Angiv {gameMode} operation for {table[i]} - "
                                    f"{tableGate[i]}: "))
                if 0 <= tableAns <= 1:
                    tableAnswer.append(tableAns)
                    print("Svar:", tableAnswer)
                    i += 1
                else:
                    print("Tallet skal være et binært tal")
            except ValueError:
                print("Det skal være et tal")

    # AND gamemode
    if gameType == 3:
        tableCAnswer = [a & b for a, b in zip(table, tableGate)]
        print("Du har tabellerne:\n", table, "\n", tableGate, "\n")
        print(f"Du skal hermed nedskrive {gameMode} operationen for de 2 tabeller")
        i = 0
        while len(tableAnswer) < tableLenght:
            try:
                tableAns = int(input(f"Angiv {gameMode} operation for {table[i]} - "
                                    f"{tableGate[i]}: "))
                if 0 <= tableAns <= 1:
                    tableAnswer.append(tableAns)
                    print("Svar:", tableAnswer)
                    i += 1
                else:
                    print("Tallet skal være et binært tal")
            except ValueError:
                print("Det skal være et tal")

    # NAND gamemode
    if gameType == 4:
        tableCAnswer = [1 - (a & b) for a, b in zip(table, tableGate)]
        print("Du har tabellerne:\n", table, "\n", tableGate, "\n")
        print(f"Du skal hermed nedskrive {gameMode} operationen for de 2 tabeller")
        i = 0
        while len(tableAnswer) < tableLenght:
            try:
                tableAns = int(input(f"Angiv {gameMode} operation for {table[i]} - "
                                    f"{tableGate[i]}: "))
                if 0 <= tableAns <= 1:
                    tableAnswer.append(tableAns)
                    print("Svar:", tableAnswer)
                    i += 1
                else:
                    print("Tallet skal være et binært tal")
            except ValueError:
                print("Det skal være et tal")

    # Spillet er Done. (a lot of print statements haha)
    if tableAnswer == tableCAnswer:
        print("\nDU VANDT!")
        print("Tillykke, du svaret rigtigt!\nDit svar:", "   ",
            tableAnswer)
        print("Rigtige svar:", tableCAnswer)
    else:
        print("\nDU TABTE!")
        print("Du fik desværre ikke svaret korrekt")
        print("Dit svar:", "   ",
            tableAnswer)
        print("Rigtige svar:", tableCAnswer)


# if main = main:
startGame(tableLenght, table, tableGate, gameModes, gameMode)
