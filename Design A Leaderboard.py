# https://leetcode.com/problems/design-a-leaderboard/

import collections, heapq

class Leaderboard:

    def __init__(self):
        self.board = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    # TC:O(NlogN), SC:O(N)
    def top(self, K: int) -> int:
        return sum(sorted(self.board.values(), reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0



class Leaderboard2:

    def __init__(self):
        self.board = collections.defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score

    # TC:O(NlogK), SC:O(K)
    def top(self, K: int) -> int:
        heap = []
        for score in self.board.values():
            if len(heap) == K:
                heapq.heappushpop(heap, score)
            else:
                heapq.heappush(heap, score)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self.board[playerId] = 0





# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)