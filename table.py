class Table:
    def __init__(self, rows, cols):
        self.table = []
        for i in range(rows):
            self.table.append([0]*cols)

    def get_value(self, row, col):
        try:
            return self.table[row][col]
        except:
            return None

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return len(self.table)

    def n_cols(self):
        return len(self.table[0])

    def delete_row(self, row):
        self.table.pop(row)

    def delete_col(self, col):
        for i in range(len(self.table)):
            self.table[i].pop(col)

    def add_row(self, row):
        self.table.insert(row, [0]*len(self.table[0]))

    def add_col(self, col):
        for i in range(len(self.table)):
            self.table[i].insert(col, 0)
