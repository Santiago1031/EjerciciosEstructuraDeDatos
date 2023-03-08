# Programa Python3 para encontrar todas las combinaciones de números
# de una cadena dada de dígitos

# función para imprimir combinaciones de números
# en la cadena de entrada dada
def printCombinations(input, index, output, outLength):
    # no quedan más dígitos en la cadena de entrada
    if (len(input) == index):
        # imprime la cadena de salida y regresa
        output[outLength] = '\0'
        print(*output[:outLength], sep="")
        return

    # coloca el dígito actual en la cadena de entrada
    output[outLength] = input[index]

    # separar el siguiente dígito con un espacio
    output[outLength + 1] = ' '
    printCombinations(input, index + 1,
                      output, outLength + 2)

    # si existe el siguiente dígito, haga un
    # llamar sin incluir espacio
    if (len(input) != (index + 1)):
        printCombinations(input, index + 1,
                          output, outLength + 1)



# código de conductor
input = "3522"
output = [0] * 100

# inicializa la salida con una cadena vacía
output[0] = '\0'
printCombinations(input, 0, output, 0)
