class Matrix:
    def __init__(self, input_v, rows):
        self.n_col = len(rows[0])
        self.n_rows = len(rows)
        self.input = input_v
        self.rows = rows

    def sort(self):
        t_input = []
        t_output = []
        n_input = len(self.input)
        for row in self.rows:
            t_input.append(row[:n_input])
            t_output.append(row[n_input:])
        print(t_input)
        print(t_output)
        

