"""Logic Gate Game - The game that will test your knowlegde on Logic gates"""

from numpy import random
from time import sleep

# Logic gates: NOT, AND, OR, NAND, NOR, XOR, XNOR
# TODO: Fix print statements
# TODO: Lav det i Pygame - Gør først dette når spillet er lavet her


class LogicGame:
    # Settings
    tableLenght = 5
    table = []
    tableGate = []
    tableAnswer = []
    tableCAnswer = []
    gameModes = ["OR", "XOR", "AND", "NOT"]
    gameMode = ""

    def __init__(self, tableLenght, table, tableGate, tableAnswer,
                 tableCAnswer, gameModes, gameMode):
        self.tableLenght = tableLenght
        self.table = table
        self.tableGate = tableGate
        self.tableAnswer = tableAnswer
        self.tableCAnswer = tableCAnswer
        self.gameModes = gameModes
        self.gameMode = gameMode

    def startGame(self, tableLenght, table, tableGate, gameModes, gameMode):
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
        LogicGame.Game(gameType)

    def Game(self, gameType):
        # OR gamemode
        if gameType == 1:
            tableCAnswer = [a | b for a, b in zip(self.table, self.tableGate)]
            print("Du har tabellerne:\n", self.table, "\n", self.tableGate, "\n")
            print(f"Du skal hermed nedskrive {self.gameMode} operationen for de 2 tabeller")
            i = 0
            while len(self.tableAnswer) < self.tableLenght:
                try:
                    tableAns = int(input(f"Angiv {self.gameMode} operation for {self.table[i]} - "
                                         f"{self.tableGate[i]}: "))
                    if 0 <= tableAns <= 1:
                        self.tableAnswer.append(tableAns)
                        print("Svar:", self.tableAnswer)
                        i += 1
                    else:
                        print("Tallet skal være et binært tal")
                except ValueError:
                    print("Det skal være et tal")

        # XOR gamemode
        if gameType == 2:
            tableCAnswer = [a ^ b for a, b in zip(self.table, self.tableGate)]
            print("Du har tabellerne:\n", self.table, "\n", self.tableGate, "\n")
            print(f"Du skal hermed nedskrive {self.gameMode} operationen for de 2 tabeller")
            i = 0
            while len(self.tableAnswer) < self.tableLenght:
                try:
                    tableAns = int(input(f"Angiv {self.gameMode} operation for {self.table[i]} - "
                                         f"{self.tableGate[i]}: "))
                    if 0 <= tableAns <= 1:
                        self.tableAnswer.append(tableAns)
                        print("Svar:", self.tableAnswer)
                        i += 1
                    else:
                        print("Tallet skal være et binært tal")
                except ValueError:
                    print("Det skal være et tal")

        # AND gamemode
        if gameType == 3:
            tableCAnswer = [a & b for a, b in zip(self.table, self.tableGate)]
            print("Du har tabellerne:\n", self.table, "\n", self.tableGate, "\n")
            print(f"Du skal hermed nedskrive {self.gameMode} operationen for de 2 tabeller")
            i = 0
            while len(self.tableAnswer) < self.tableLenght:
                try:
                    tableAns = int(input(f"Angiv {self.gameMode} operation for {self.table[i]} - "
                                         f"{self.tableGate[i]}: "))
                    if 0 <= tableAns <= 1:
                        self.tableAnswer.append(tableAns)
                        print("Svar:", self.tableAnswer)
                        i += 1
                    else:
                        print("Tallet skal være et binært tal")
                except ValueError:
                    print("Det skal være et tal")

        # NAND gamemode
        if gameType == 4:
            tableCAnswer = [1 - (a & b) for a, b in zip(self.table, self.tableGate)]
            print("Du har tabellerne:\n", self.table, "\n", self.tableGate, "\n")
            print(f"Du skal hermed nedskrive {self.gameMode} operationen for de 2 tabeller")
            i = 0
            while len(self.tableAnswer) < self.tableLenght:
                try:
                    tableAns = int(input(f"Angiv {self.gameMode} operation for {self.table[i]} - "
                                         f"{self.tableGate[i]}: "))
                    if 0 <= tableAns <= 1:
                        self.tableAnswer.append(tableAns)
                        print("Svar:", self.tableAnswer)
                        i += 1
                    else:
                        print("Tallet skal være et binært tal")
                except ValueError:
                    print("Det skal være et tal")

        # Spillet er Done. (a lot of print statements haha)
        if self.tableAnswer == tableCAnswer:
            print("\nDU VANDT!")
            print("Tillykke, du svaret rigtigt!\nDit svar:", "   ",
                  self.tableAnswer)
            print("Rigtige svar:", tableCAnswer)
        else:
            print("\nDU TABTE!")
            print("Du fik desværre ikke svaret korrekt")
            print("Dit svar:", "   ",
                  self.tableAnswer)
            print("Rigtige svar:", tableCAnswer)


# if main = main:
LogicGame.startGame()
