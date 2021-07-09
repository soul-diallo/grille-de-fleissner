import random
import string


def convertLetters(text):
    for i in range(len(text) - 1):
        # Removing the space
        if text[i] == ' ':
            text = text.replace(text[i], '')
            return text
    return text


def completion(text, n):
    aleaStr = ''
    alpha = string.ascii_lowercase
    for i in range(n):
        alea = random.randint(0, 25)
        aleaStr += alpha[alea]
    text += aleaStr
    return text


def rotation(grid, n, clock):
    tab = []
    for i in range(n):
        for k in range(n):
            tab.append(grid[k][len(grid)-1-i])
    return tab


print(len([[0, 1, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 1, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0, 0]]))


def correct(grid, n):
    etat = False
    return etat


def randomGrid(n):
    grid = []
    return grid


def loadGrid(file):
    pass


def saveGrid(grid, n, file):
    pass


def cipher(grid, n, text, clock):
    pass


def squareToText(square, n):
    pass


def cipherFleissner(grid, n, text, clock):
    pass


def textToSquare(text, n):
    pass


def decipher(grid, n, square, clock):
    pass


def decipherFleissner(grid, n, text, clock):
    pass
