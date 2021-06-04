import coord as c
n = int(input("Inserire lunghezza coordinata: "))
a = c.Coord(n)

for i in range(pow(2, a.num_v) - 1):
    print(a.incrementOne())
