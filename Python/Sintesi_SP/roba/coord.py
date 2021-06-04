class Coord:
    #/ Es. 001 ----> Coordinata da 3 valori: [0,0,1]
    def __init__(self, num_v):
        self.num_v = num_v
        self.val = []
        self.setToZero()
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


    def incrementOne(self):
        temp_bin = []
        temp_bin += self.val
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
        self.val = temp_bin
        temp_bin = self.fromBintoGray(temp_bin)
        return temp_bin
