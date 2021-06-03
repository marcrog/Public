class Map:
    def __init__(self, list_input, list_output, str_all):
        #Number of elements
        self.n_output = len(list_output)
        self.n_input = len(list_input)
        #List input-output (as coordinate objects)
        self.input = list_input
        self.output = list_output
        #List of Rows
        self.rows = self.makeRows(str_all)
        
    def makeRows (self, str_all):
        start_str = str_all
        num_to_split = self.n_input + self.n_output
        inc2 = num_to_split
        inc1 = 0
        result = []
        while inc2 <= len(str_all):
            result.append(start_str[inc1:inc2])
            inc1 += num_to_split
            inc2 += num_to_split
        return result
    
    def coordAssigment(self, n_coord):
        #/ Input bits calculation
            print("Too many input variables")
            return -1
        assign_l = [0,0,1,1,2,2]
        left_bits = assign_l[n_coord]
        if self.n_input == 5 and self.n_output == 1 :
            self.n_output += 1
            left_bits -= 1
        top_bits = self.n_input - left_bits
        result = [left_bits, top_bits]
        return result

    def createCoordinate(self, num):
        _len = pow(2, num) / 2
        resutl =[]
        for x in range(_len):
            temp = []

      
    def fromBintoGray(self,binary):
        b = binary
        gray = [b[0]]
        p = b[0]
        b.pop(0)
        for current in b:
            gray.append(self._xor[p,current])
            p = current
        return gray


