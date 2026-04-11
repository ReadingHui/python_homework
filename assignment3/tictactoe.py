# Task 6: More on Classes
class TictactoeException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
    
class Board():
    valid_moves = ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]

    def __init__(self):
        self.board_array = [[" " for c in range(3)] for r in range(3)]
        self.turn = 'X'
        return
    
    def __str__(self):
        h_line = '-------\n'
        rows = ['|' + '|'.join(self.board_array[r]) + '|\n' for r in range(3)]
        return h_line + h_line.join(rows) + h_line
    
    def move(self, move_string):
        if move_string not in Board.valid_moves:
            raise TictactoeException("That's not a valid move.")
        move_ind = Board.valid_moves.index(move_string)
        row = move_ind // 3
        col = move_ind % 3
        if self.board_array[row][col] != ' ':
            raise TictactoeException('The spot is already taken!')
        else:
            self.board_array[row][col] = self.turn
            if self.turn == 'X':
                self.turn = 'O'
            else:
                self.turn = 'X'
    
    def whats_next(self):
        def check_empty():
            for i in range(3):
                for j in range(3):
                    if self.board_array[i][j] == ' ':
                        return True
            return False
        
        def check_row(row):
            if row == ['X', 'X', 'X']:
                return (True, 'X has won')
            if row == ['O', 'O', 'O']:
                return (True, 'O has won')
            else:
                return (False, "Cat's Game")

    
        for row in range(3):
            result = check_row(self.board_array[row])
            if result[0]:
                return result
        for col in range(3):
            new_row = [self.board_array[r][col] for r in range(3)]
            result = check_row(new_row)
            if result[0]:
                return result
        new_row = [self.board_array[r][r] for r in range(3)]
        result = check_row(new_row)
        if result[0]:
            return result
        new_row = [self.board_array[r][2-r] for r in range(3)]
        result = check_row(new_row)
        if result[0]:
            return result
        if check_empty():
            return (False, f"{self.turn}'s turn")
        else:
            return (True, "Cat's Game")

def main():     
    board = Board()
    steps = 0
    print(f'Step {steps}: ')
    print(board)
    result = board.whats_next()

    while not result[0]:
        print(result[1])
        move_string = input('Where is your next move? Choose from ["upper left", "upper center", "upper right", "middle left", "center", "middle right", "lower left", "lower center", "lower right"]')
        try:
            board.move(move_string)
        except TictactoeException as e:
            print(e)
        steps += 1
        print(f'Step {steps}: ')
        print(board)
        result = board.whats_next()
    
    print(f'Game Over! {result[1]}!')

if __name__ == '__main__':
    main()