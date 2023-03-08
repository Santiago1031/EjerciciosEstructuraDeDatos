
def myAtoiRecursive(string, num):
    # Si str es NULL o str contiene no numérico
    # caracteres luego devuelven 0 ya que el número no es
    # válido
    if string.isalpha():
        return 0;

    if (len(string) == 0):
        return 0;
    # caso base, hemos llegado al final de la cadena,
    # simplemente devolvemos el último valor
    if len(string) == 1:
        return int(string) + (num * 10)

    # agregar el siguiente elemento de cadena en nuestro valor numérico
    num = int(string[0:1]) + (num * 10)

    # recurse por el resto de la cadena
    # y agregue cada letra a num
    return myAtoiRecursive(string[1:], num)


# código de conductor
string = "103"

print(myAtoiRecursive(string, 3))
