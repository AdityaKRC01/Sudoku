class Board:

    def __init__(self):
        pass

    def generate_board(self):
        b = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        self.print_board(b)

        while True:

            print(
                'Kindly Provide the Column and Row where you would like to place a value:')

            c = int(input('Column: '))
            r = int(input('Row: '))

            value = input(
                'What Value (1-9) would you like to place in the board? Type Q to stop placing values\n')

            if value.upper() == 'Q':
                print('\n'*100)
                self.print_board(b)
                end = input(
                    'Is this the correct board you intend to solve? Answer with Y or N')
                if end.upper() == 'Y':
                    break
                else:
                    continue

            else:
                b[r-1][c-1] = value
                print('\n'*100)
                self.print_board(b)

        return b

    def print_board(self, b):
        print('---+-------+-------+-------+')
        print('   | 1 2 3 | 4 5 6 | 7 8 9 |')
        print('---+-------+-------+-------+')
        print(
            f' 1 | {b[0][0]} {b[0][1]} {b[0][2]} | {b[0][3]} {b[0][4]} {b[0][5]} | {b[0][6]} {b[0][7]} {b[0][8]} |')
        print(
            f' 2 | {b[1][0]} {b[1][1]} {b[1][2]} | {b[1][3]} {b[1][4]} {b[1][5]} | {b[1][6]} {b[1][7]} {b[1][8]} |')
        print(
            f' 3 | {b[2][0]} {b[2][1]} {b[2][2]} | {b[2][3]} {b[2][4]} {b[2][5]} | {b[2][6]} {b[2][7]} {b[2][8]} |')
        print('---+-------+-------+-------+')
        print(
            f' 4 | {b[3][0]} {b[3][1]} {b[3][2]} | {b[3][3]} {b[3][4]} {b[3][5]} | {b[3][6]} {b[3][7]} {b[3][8]} |')
        print(
            f' 5 | {b[4][0]} {b[4][1]} {b[4][2]} | {b[4][3]} {b[4][4]} {b[4][5]} | {b[4][6]} {b[4][7]} {b[4][8]} |')
        print(
            f' 6 | {b[5][0]} {b[5][1]} {b[5][2]} | {b[5][3]} {b[5][4]} {b[5][5]} | {b[5][6]} {b[5][7]} {b[5][8]} |')
        print('---+-------+-------+-------+')
        print(
            f' 7 | {b[6][0]} {b[6][1]} {b[6][2]} | {b[6][3]} {b[6][4]} {b[6][5]} | {b[6][6]} {b[6][7]} {b[6][8]} |')
        print(
            f' 8 | {b[7][0]} {b[7][1]} {b[7][2]} | {b[7][3]} {b[7][4]} {b[7][5]} | {b[7][6]} {b[7][7]} {b[7][8]} |')
        print(
            f' 9 | {b[8][0]} {b[8][1]} {b[8][2]} | {b[8][3]} {b[8][4]} {b[8][5]} | {b[8][6]} {b[8][7]} {b[8][8]} |')
        print('---+-------+-------+-------+')
