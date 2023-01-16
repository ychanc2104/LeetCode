# https://leetcode.com/problems/design-snake-game/

import collections

class SnakeGame:

    # TC:O(1), SC:O(1)
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.n = height
        self.m = width
        self.food = food
        self.i = 0
        self.snake = collections.deque([[0, 0]])
        self.body = set()  # hash set to store body (exclude head and tail)
        self.dir_opt = {'R': [0, 1], 'L': [0, -1], 'U': [-1, 0], 'D': [1, 0]}

    # TC:O(1), SC:O(WH+N) to store snake and food
    def move(self, direction: str) -> int:
        ro, co = self.dir_opt[direction]
        r, c = self.snake[0]
        rn, cn = r + ro, c + co  # new head
        # check out of bound
        if not 0 <= rn < self.n or not 0 <= cn < self.m:
            return -1
        # check hit body
        if (rn, cn) in self.body:
            return -1
        self.snake.appendleft([rn, cn])
        # check hit the food
        if self.i < len(self.food) and [rn, cn] == self.food[self.i]:
            self.i += 1
            if self.i > 1:  # have body
                # add old head
                self.body.add((r, c))
        else:  # remove tail
            self.snake.pop()
            if self.i > 1:
                # add old head
                self.body.add((r, c))
                # remove current tail
                self.body.remove(tuple(self.snake[-1]))

        return self.i

# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)