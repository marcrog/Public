import coord as c
n = int(input("Inserire lunghezza coordinata: "))
a = c.Coord(n)

for i in range(pow(2, a.num_v)):
    if i == 0:
        print(a.val)
    else:
        print(a.incrementOne())
