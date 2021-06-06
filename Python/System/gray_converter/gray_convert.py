def somm_next(b1, b2):
    if b2 == 1:
        if b1 == 0:
            return 1
        else:
            return 0
    else:
        return b1

def togray(binary):
    new = ""
    for x in range(len(binary)):
        if len(binary) == 1:
            new = new + binary[0]
        else:
            new = new + str(somm_next(int(binary[-1]),int( binary[-2])))
            binary = binary[:-1]

        new = new[-1] + new[:-1]
    return new



input = input("Inserire numero in binario: ")
print("\n" + "Il numero convertito con nel codice di gray è: " + togray(input))

