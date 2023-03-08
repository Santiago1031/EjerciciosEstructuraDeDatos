def generate_binary_strings(n: int):
    if n == 0:
        return [""]
    if n == 1:
        return ["0", "1"]
    result = []
    for s in generate_binary_strings(n - 1):
        result.append(s + "0")
        if s[-1] != "1":
            result.append(s + "1")
    return result


# ejemplo de uso
arr = generate_binary_strings(2)
for i in arr:
    print(i, end=' ')
