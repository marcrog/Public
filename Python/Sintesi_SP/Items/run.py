import items as i

a = i.Map(["A", "B", "C", "D",], ["U"], "000100100100100001111111")
print(a.input)
print(a.output)
print(a.rows)
print(a.coordAssigment())
print(a.createCoordinate(2))

l = input("Inseire lista di input: ")
if a.findOutput(l) != []:
    print("output = ", end="")
    print(a.findOutput(l))
else:
    print("Non esiste questa combinazione")
