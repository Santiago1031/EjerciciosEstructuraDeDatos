# Programa Python para calcular
# longitud de una cadena usando
# recursión
str = "AveMariaSantisima"


# Función para
# calcular la longitud
def string_length(str):
    # si llegamos al
    # final de la cadena
    if str == '':
        return 0
    else:
        return 1 + string_length(str[1:])

# código de conductor
print(string_length(str))