def howManyMissing(lista: list[int]) -> int:
    missing = 0
    index = 0
    for i in range(lista[0],lista[len(lista)-1]):
        if i != lista[index]:
            i += 1
            missing += 1
        else:
            index += 1
    return missing