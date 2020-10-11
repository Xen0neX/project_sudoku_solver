# Arihant Kuba

class SudokuSquare:
    '''Class defining the sudoku as a part of its cells'''
    def __init__ (self, row_num, col_num, box_num, value, guess, solved):
        self.row_num = 0
        self.col_num = 0
        self.box_num = 0
        self.value = 0
        self.guess = []
        self.solved = False
