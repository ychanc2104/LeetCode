# https://leetcode.com/problems/design-tic-tac-toe/description/
# https://leetcode.com/problems/design-tic-tac-toe/solutions/81932/python-13-lines-easy-to-understand/


# TC:O(1) for move, SC:O(N)
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.moves = {
            1:{'row':{i:set() for i in range(n)}, 'col':{i:set() for i in range(n)}, 'd':0, 'ad':0},
            2:{'row':{i:set() for i in range(n)}, 'col':{i:set() for i in range(n)}, 'd':0, 'ad':0}}

    def move(self, row: int, col: int, player: int) -> int:
        self.moves[player]['row'][col].add(row)
        self.moves[player]['col'][row].add(col)
        self.moves[player]['d'] += 1 if row-col == 0 else 0
        self.moves[player]['ad'] += 1 if row+col == self.n-1 else 0
        if len(self.moves[player]['row'][col]) == self.n:
            return player
        if len(self.moves[player]['col'][row]) == self.n:
            return player
        if self.moves[player]['d'] == self.n:
            return player
        if self.moves[player]['ad'] == self.n:
            return player
        return 0


# space optimized, TC:O(1), SC:O(N)
class TicTacToe2:

    def __init__(self, n: int):
        self.n = n
        self.moves = {
            1:{'row':{i:0 for i in range(n)}, 'col':{i:0 for i in range(n)}, 'd':0, 'ad':0},
            2:{'row':{i:0 for i in range(n)}, 'col':{i:0 for i in range(n)}, 'd':0, 'ad':0}}

    def move(self, row: int, col: int, player: int) -> int:
        self.moves[player]['row'][col] += 1
        self.moves[player]['col'][row] += 1
        self.moves[player]['d'] += 1 if row-col == 0 else 0
        self.moves[player]['ad'] += 1 if row+col == self.n-1 else 0
        if self.n in [self.moves[player]['row'][col], self.moves[player]['col'][row], self.moves[player]['d'], self.moves[player]['ad']]:
            return player
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)