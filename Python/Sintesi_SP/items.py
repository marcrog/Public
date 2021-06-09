import Matrix.matrix as m

def makeRows (n_input, n_output, str_all):
    start_str = str_all
    num_to_split = n_input + n_output
    inc2 = num_to_split
    inc1 = 0
    result = []
    while inc2 <= len(str_all):
        result.append(start_str[inc1:inc2])
        inc1 += num_to_split
        inc2 += num_to_split
    return result


class Map:
    def __init__(self, list_input, list_output, str_all):
        #Number of elements
        self.n_output = len(list_output)
        self.n_input = len(list_input)
        #List input-output (as coordinate objects)
        self.input = list_input
        self.output = list_output
        #List of Rows
        self.rows = makeRows(self.n_input, self.n_output, str_all)
        #self.rows = makeRows(3,1, str_all)
        #Coordinates
        self.left_num_c = 0
        self.top_num_c = 0
        self.tab_num_c = 0
        self.n_map = self.n_output
        
    
    def coordAssigment(self):
        assign_l = {
            2 : 1,
            3 : 1,
            4 : 2,
            5 : 2,
            6 : 2
        }
        #/ Input bits calculation
        if self.n_input > 6:
            print("Too many input variables")
            return -1
        self.tab_bits = 1
        self.left_num_c = assign_l[self.n_input]
        self.top_num_c = self.n_input - self.left_num_c
        if self.n_input >= 5:
            self.tab_num_c = (self.n_input - 5) + 1
            self.top_num_c = 2
        result = [self.left_num_c, self.top_num_c, self.tab_num_c]
        return result


    def createMatrix(self):
        #Matrix with max 4 inputs
        matrix = m.Matrix(self.input, self.rows)


    # def findOutput(self, l):
        # i = 0
        # rows = []
        # rows += self.rows
        # for row in rows:

            # output = row[-1]
            # row.pop(-1)
            # for bit in row:
                # if bit == l[i]:
                    # i += 1
            # if i == len(l):
                # return output
            # i = 0
        # return []
      


