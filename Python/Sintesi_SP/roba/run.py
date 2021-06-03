import coord as c

a = c.Coord(4)

for i in range(16):
    a.incrementOne()
    print(a.val)
