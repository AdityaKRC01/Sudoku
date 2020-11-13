class ValidEntry:

    def __init__(self):
        pass

    def valid_val(self, board, row, column, value):
        #Checks Row for same value
        for i in range(9):
            if board[row][i] == value:
                return False 

        #Checks Column  For same Value
        for i in range(9):
            if board[i][column] == value:
                return False 

        #Checks sub-grid for same value
        x = (column//3)*3
        y= (row//3)*3

        for i in range(0,3):
            for j in range(0,3):
                if board[y+i][x+j] == value:
                    return False

        return True


        
        

        
