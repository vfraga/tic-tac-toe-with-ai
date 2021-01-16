import random


class Table:
    table = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    def checkhorizontal(self) -> tuple:
        if self.table[0][0] == 'X' and self.table[0][1] == 'X' and self.table[0][2] == 'X':
            return True, 'X'
        elif self.table[1][0] == 'X' and self.table[1][1] == 'X' and self.table[1][2] == 'X':
            return True, 'X'
        elif self.table[2][0] == 'X' and self.table[2][1] == 'X' and self.table[2][2] == 'X':
            return True, 'X'
        elif self.table[0][0] == 'O' and self.table[0][1] == 'O' and self.table[0][2] == 'O':
            return True, 'O'
        elif self.table[1][0] == 'O' and self.table[1][1] == 'O' and self.table[1][2] == 'O':
            return True, 'O'
        elif self.table[2][0] == 'O' and self.table[2][1] == 'O' and self.table[2][2] == 'O':
            return True, 'O'
        else:
            return False, None

    def checkdiagonal(self) -> tuple:
        if self.table[0][0] == 'X' and self.table[1][1] == 'X' and self.table[2][2] == 'X':
            return True, 'X'
        elif self.table[0][2] == 'X' and self.table[1][1] == 'X' and self.table[2][0] == 'X':
            return True, 'X'
        elif self.table[0][0] == 'O' and self.table[1][1] == 'O' and self.table[2][2] == 'O':
            return True, 'O'
        elif self.table[0][2] == 'O' and self.table[1][1] == 'O' and self.table[2][0] == 'O':
            return True, 'O'
        else:
            return False, None

    def checkvertical(self) -> tuple:
        if self.table[0][0] == 'X' and self.table[1][0] == 'X' and self.table[2][0] == 'X':
            return True, 'X'
        elif self.table[0][1] == 'X' and self.table[1][1] == 'X' and self.table[2][1] == 'X':
            return True, 'X'
        elif self.table[0][2] == 'X' and self.table[1][2] == 'X' and self.table[2][2] == 'X':
            return True, 'X'
        elif self.table[0][0] == 'O' and self.table[1][0] == 'O' and self.table[2][0] == 'O':
            return True, 'O'
        elif self.table[0][1] == 'O' and self.table[1][1] == 'O' and self.table[2][1] == 'O':
            return True, 'O'
        elif self.table[0][2] == 'O' and self.table[1][2] == 'O' and self.table[2][2] == 'O':
            return True, 'O'
        else:
            return False, None

    def hasempty(self) -> bool:
        for row in self.table:
            for item in row:
                if item == ' ':
                    return True
        return False

    def settable(self) -> str:
        input_str = input('Enter the cells: ')
        acceptable_chars = ['_', 'X', 'O']
        print(len(input_str))
        if all([x in acceptable_chars for x in input_str]) and len(input_str) == 9:
            count = 0
            for i in range(3):
                for j in range(3):
                    self.table[i][j] = input_str[count]
                    count += 1
            return 'O' if len([char for char in input_str if char == '_']) % 2 == 0 else 'X'

    def cleargame(self) -> str:
        for i in range(3):
            for j in range(3):
                self.table[i][j] = ' '
        return 'X'

    def showtable(self) -> None:
        ui_dict = {0: f'---------',
                   1: f'| {self.table[0][0]} {self.table[0][1]} {self.table[0][2]} |',
                   2: f'| {self.table[1][0]} {self.table[1][1]} {self.table[1][2]} |',
                   3: f'| {self.table[2][0]} {self.table[2][1]} {self.table[2][2]} |',
                   4: f'---------'}
        for row in ui_dict.values():
            print(row)


class Game(Table):
    next_move = 'X'
    player1_move = 'X'
    player2_move = 'O'
    bot_moves = []
    player_moves = []

    def __init__(self):
        self.player1 = None
        self.player2 = None

    def printgamestate(self) -> None:
        if any([self.checkvertical()[0], self.checkhorizontal()[0], self.checkdiagonal()[0]]):
            won = [self.checkvertical()[1], self.checkhorizontal()[1], self.checkdiagonal()[1]]
            if 'X' in won and 'O' not in won:
                print('X wins')
                return None
            elif 'O' in won and 'X' not in won:
                print('O wins')
                return None
        elif not any([self.checkvertical()[0], self.checkhorizontal()[0], self.checkdiagonal()[0]]) and self.hasempty():
            print('Game not finished')
            return None
        else:
            print('Draw')
            return None

    def running(self) -> bool:
        if any([self.checkvertical()[0], self.checkhorizontal()[0], self.checkdiagonal()[0]]):
            return False
        elif not any([self.checkvertical()[0], self.checkhorizontal()[0], self.checkdiagonal()[0]]):
            if self.hasempty():
                return True
            else:
                return False
        else:
            return False

    def usermove(self) -> None:
        if self.next_move in self.player_moves and self.running():
            input_str = input('Enter the coordinates: ')
            nums = input_str.split()
            if all([x.isdecimal() for x in nums]):
                nums = [int(x) for x in nums]
                x, y = nums[0], nums[1]
                del nums
                if (x < 1 or x > 3) or (y < 1 or y > 3):
                    print('Coordinates should be from 1 to 3!')
                    self.usermove()
                elif self.table[x - 1][y - 1] != ' ':
                    print('This cell is occupied! Choose another one!')
                    self.usermove()
                elif self.next_move in self.player_moves and self.running():
                    self.table[x - 1][y - 1] = self.next_move
                    self.next_move = 'O' if self.next_move == 'X' else 'X'
                    self.showtable()
            else:
                print('You should enter numbers!')
                self.usermove()

    def easymove(self) -> None:
        if self.next_move in self.bot_moves and self.running():
            x, y = (random.randint(0, 2), random.randint(0, 2))
            while self.table[x][y] != ' ' and self.hasempty():
                x, y = (random.randint(0, 2), random.randint(0, 2))
            self.table[x][y] = self.next_move
            print('Making move level "easy"')
            self.showtable()
            self.next_move = 'O' if self.next_move == 'X' else 'X'

    def mediummove(self) -> None:
        if self.next_move in self.bot_moves and self.running():
            enemy, move = [val for val in ['X', 'O'] if val != self.next_move][0], self.next_move

            # Checks for prioritised horizontal moves
            for i in range(3):
                if (self.table[i].count(move) == 2 and self.table[i].count(enemy) == 0) \
                        or (self.table[i].count(enemy) == 2 and self.table[i].count(move) == 0):
                    x, y = i, 0
                    while self.table[i][y] != ' ' and self.hasempty():
                        y = random.randint(1, 2)
                    self.table[x][y] = move
                    print('Making move level "medium"')
                    self.showtable()
                    self.next_move = 'O' if self.next_move == 'X' else 'X'
                    return None

            # Checks for prioritised vertical moves
            for i in range(3):
                sequence_enemy = 0
                sequence_ally = 0
                for j in range(3):
                    if self.table[j][i] == move:
                        sequence_ally += 1
                        sequence_enemy -= 1
                    elif self.table[j][i] == enemy:
                        sequence_ally -= 1
                        sequence_enemy += 1
                    if j == 2 and any([sequence_ally == 2, sequence_enemy == 2]):
                        while self.table[j][i] != ' ' and self.hasempty():
                            j = random.randint(0, 2)
                        self.table[j][i] = move
                        print('Making move level "medium"')
                        self.showtable()
                        self.next_move = 'O' if self.next_move == 'X' else 'X'
                        return None

            # Checks for prioritised diagonal moves
            sequence_ally = 0
            sequence_enemy = 0
            for i in range(3):
                if self.table[i][i] == move:
                    sequence_ally += 1
                    sequence_enemy -= 1
                elif self.table[i][i] == enemy:
                    sequence_ally -= 1
                    sequence_enemy += 1
                if i == 2 and any([sequence_ally == 2, sequence_enemy == 2]):
                    while self.table[i][i] != ' ' and self.hasempty():
                        i = random.randint(0, 2)
                    print('Making move level "medium"')
                    self.table[i][i] = move
                    self.showtable()
                    self.next_move = 'O' if self.next_move == 'X' else 'X'
                    return None

            # Checks for prioritised 2nd diagonal moves
            sequence_ally = 0
            sequence_enemy = 0
            for i, j in enumerate(range(2, -1, -1)):
                if self.table[i][j] == move:
                    sequence_ally += 1
                    sequence_enemy -= 1
                elif self.table[i][j] == enemy:
                    sequence_ally -= 1
                    sequence_enemy += 1
                if i == 2 and any([sequence_ally == 2, sequence_enemy == 2]):
                    if self.hasempty():
                        for x, y in enumerate(range(2, -1, -1)):
                            if self.table[x][y] == ' ':
                                self.table[x][y] = move
                    print('Making move level "medium"')
                    self.showtable()
                    self.next_move = 'O' if self.next_move == 'X' else 'X'
                    return None

            # If no prioritised moves are to be performed, makes a random move
            x, y = (random.randint(0, 2), random.randint(0, 2))
            while self.table[x][y] != ' ' and self.hasempty():
                x, y = (random.randint(0, 2), random.randint(0, 2))
            if self.next_move in self.bot_moves and self.running():
                self.table[x][y] = self.next_move
                print('Making move level "medium"')
                self.showtable()
                self.next_move = 'O' if self.next_move == 'X' else 'X'
        else:
            return None

    def max(self):
        move, enemy = self.next_move, [x for x in ['X', 'O'] if x != self.next_move][0]
        maxv, x, y = -2, None, None

        result = self.checkdiagonal()[1] or self.checkvertical()[1] or self.checkhorizontal()[1]
        if result is None:
            result = ' '

        if result == enemy:
            return -1, 0, 0
        if result == move:
            return 1, 0, 0
        if not self.hasempty():
            if result == ' ':
                return 0, 0, 0

        for i in range(3):
            for j in range(3):
                if self.table[i][j] == ' ':
                    self.table[i][j] = move
                    m, min_i, min_j = self.min()
                    if m > maxv:
                        maxv = m
                        x = i
                        y = j
                    self.table[i][j] = ' '

        return maxv, x, y

    def min(self):
        move, enemy = self.next_move, [x for x in ['X', 'O'] if x != self.next_move][0]
        minv, x, y = 2, None, None

        result = self.checkdiagonal()[1] or self.checkvertical()[1] or self.checkhorizontal()[1]
        if result is None:
            result = ' '

        if result == enemy:
            return -1, 0, 0
        if result == move:
            return 1, 0, 0
        if not self.hasempty():
            if result == ' ':
                return 0, 0, 0

        for i in range(0, 3):
            for j in range(0, 3):
                if self.table[i][j] == ' ':
                    self.table[i][j] = enemy
                    (m, max_i, max_j) = self.max()
                    if m < minv:
                        minv = m
                        x = i
                        y = j
                    self.table[i][j] = ' '
        return minv, x, y

    def hardmove(self):
        m, x, y = self.max()
        if self.next_move in self.bot_moves and self.running():
            self.table[x][y] = self.next_move
            print('Making move level "hard"')
            self.showtable()
            self.next_move = 'O' if self.next_move == 'X' else 'X'

    def botmove(self):
        if self.running():
            if 'X' == self.next_move and self.player1 != 'user':
                if self.player1 == 'easy':
                    self.easymove()
                elif self.player1 == 'medium':
                    self.mediummove()
                elif self.player1 == 'hard':
                    self.hardmove()
            elif 'O' == self.next_move and self.player2 != 'user':
                if self.player2 == 'easy':
                    self.easymove()
                elif self.player2 == 'medium':
                    self.mediummove()
                elif self.player2 == 'hard':
                    self.hardmove()

    def move(self):
        if self.running():
            if 'X' == self.next_move and self.player1 == 'user':
                self.usermove()
            elif 'X' == self.next_move and self.player1 != 'user':
                self.botmove()
            elif 'O' == self.next_move and self.player2 == 'user':
                self.usermove()
            elif 'O' == self.next_move and self.player2 != 'user':
                self.botmove()

    def start(self, input_str: str) -> None:
        user_in = input_str.lower().split()
        valid_inputs = ['easy', 'medium', 'hard', 'user']
        if len(user_in) != 3:
            print('Bad parameters!')
        elif user_in[0] == 'start' and user_in[1] not in valid_inputs or user_in[2] not in valid_inputs:
            print('Bad parameters!')
        elif user_in[0] == 'start' and user_in[1] in valid_inputs and user_in[2] in valid_inputs:
            self.player1, self.player2 = user_in[1], user_in[2]

            if user_in[1] != 'user':
                self.bot_moves.append(self.player1_move)
            elif user_in[1] == 'user':
                self.player_moves.append(self.player1_move)
            if user_in[2] != 'user':
                self.bot_moves.append(self.player2_move)
            elif user_in[2] == 'user':
                self.player_moves.append(self.player2_move)

            while self.running():
                self.move()
            self.printgamestate()
            self.cleargame()
            return None

        elif 'exit' in user_in:
            return None
        else:
            print('Bad parameters!')
            return None


def menu() -> None:
    user_in = input('Input command: ')
    while 'exit' not in user_in:
        x = Game()
        x.start(user_in)
        user_in = input('Input command: ')


if __name__ == '__main__':
    menu()
