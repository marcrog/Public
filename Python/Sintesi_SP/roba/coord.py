class Coord:
    #/ Es. 001 ----> Coordinata da 3 valori: [0,0,1]
    def __init__(self, num_v):
        self.num_v = num_v
        self.val = []
        self.setToZero()
        print(self.val)
        self._xor = {
            (0, 0): 0,
            (0, 1): 1,
            (1, 0): 1,
            (1, 1): 0
        }

    def setValues(self, list_values):
        self.val = list_values
    
    def setToZero(self):
        self.val = []
        for x in range(self.num_v):
            self.val.append(0)
    
    def toZero(self):
        val = []
        for x in range(self.num_v):
            val.append(0)
        return val

    def fromGraytoBin(self):
        temp = self.val
        binary = [temp[0]]
        p = temp[0]
        temp.pop(0)
        for current in temp:
            binary.append(self._xor[p,current])
            p = binary[-1]
        return binary

    def fromBintoGray(self,binary):
        b = []
        b = b + binary
        gray = [b[0]]
        p = b[0]
        b.pop(0)
        for current in b:
            gray.append(self._xor[p,current])
            p = current
        return gray

    def setBin(self, int_):
        self.setToZero()
        for i  in range(int_):
            self.incrementOne()
        pass

    def incrementOne(self):
        temp_bin = self.val
        gray = self.fromBintoGray(temp_bin)
        if temp_bin != gray and temp_bin != self.toZero():
            print("Uguale")
            return gray
        print("Diversi")
        resto = 1
        i = self.num_v - 1
        while resto == 1 and i >= 0:
            if temp_bin[i] == 1:
                temp_bin[i] = 0
                resto = 1
            else:
                temp_bin[i] = 1
                resto = 0
            i -= 1
        return temp_bin
