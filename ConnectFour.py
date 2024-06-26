#I've created 2 class (Player & Board)

class Player:
    def __init__(self, name, symbol):    #A player has a name & symbol variable
        self.name = name
        self.symbol = symbol

class Board:
    def __init__(self, rows=6, columns=7):  #Going to create a 6X7 Grid
        self.rows = rows
        self.columns = columns
        self.grid = [[' ' for _ in range(columns)] for _ in range(rows)]
        self.current_player = None

    def display(self):
        print('\n'.join(['|'.join(row) for row in self.grid]))
        print('-' * (self.columns * 2 - 1))
        print(' '.join(map(str, range(self.columns))))

    def is_valid_column(self, column):
        return 0 <= column < self.columns and self.grid[0][column] == ' '

    def drop_disc(self, column, symbol):
        for row in reversed(self.grid):
            if row[column] == ' ':
                row[column] = symbol
                break

    def check_winner(self, symbol):
        # Check horizontal
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if all(self.grid[row][col + i] == symbol for i in range(4)):
                    return True

        # Check vertical
        for row in range(self.rows - 3):
            for col in range(self.columns):
                if all(self.grid[row + i][col] == symbol for i in range(4)):
                    return True

        # Check positive diagonal
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if all(self.grid[row + i][col + i] == symbol for i in range(4)):
                    return True

        # Check negative diagonal
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if all(self.grid[row - i][col + i] == symbol for i in range(4)):
                    return True

        return False

    def is_full(self):
        return all(self.grid[0][col] != ' ' for col in range(self.columns))

    def switch_player(self, player1, player2):
        self.current_player = player2 if self.current_player == player1 else player1

def main():
    player1 = Player(input("Enter Player 1's name: "), 'X')
    player2 = Player(input("Enter Player 2's name: "), 'O')
    board = Board()
    board.current_player = player1

    while True:
        board.display()

