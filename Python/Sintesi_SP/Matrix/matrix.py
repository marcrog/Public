class Matrix:
    #def __init__(self, n_columns, n_rows, input_vairables, rows):
    def __init__(self, n_columns, n_rows, rows):
        self.n_col = n_columns
        self.n_rows = n_rows
        #self.input = input_variables
        self.rows = rows

    def sort(self):
        t_input = []
        t_output = []
        #n_input = len(self.input)
        n_input = 2
        for row in self.rows:
            t_input.insert(0,row[n_input:])
            t_output.insert(0,row[:n_input])
        print(t_input)
        print(t_output)
        

