import numpy as np

diemes_matriz = np.array([[3, 4, 1], [3, 1, 2]])
soma = 0

for linha in diemes_matriz:

    for elemento in linha:
        soma += elemento

print("A soma de todos os elementos da matriz acima é:", soma)