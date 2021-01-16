class Matrix:
    def __init__(self, matrix_string):
        self.rows = matrix_string.splitlines()


    def row(self, index):
        if index < 1:
            raise AssertionError("dontdothat")
        return [int(i) for i in self.rows[index-1].split(' ')]
        

    def column(self, index):
        col = []
        for i in self.rows:
            n = i.split(' ')
            col.append(int(n[index-1]))

        return col