# Función para encontrar la cadena que tiene
# primer carácter de cada palabra.

def first(word):
    for i in range(0, len(word)):

        if (word[i].isupper()):
            return word[i]

    return "No contiene mayuscula :/"


# Driver code
word = "cristianoRonaldo"
print(first(word))