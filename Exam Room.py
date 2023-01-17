# https://leetcode.com/problems/exam-room/
# https://leetcode.com/problems/exam-room/solutions/185690/python-heapq-clean-solution-with-explanation-seat-o-log-n-leave-o-n/


import heapq

class ExamRoom:

    # SC:O(N)
    def __init__(self, n: int):
        self.n = n
        self.seats = [(-(n + 1) // 2, -1, n)]  # put intervals (heap)

    # TC:O(logN)
    def seat(self) -> int:
        interval, L, R = heapq.heappop(self.seats)  # pop out max interval
        if L == -1:
            pos = 0
        elif R == self.n:
            pos = self.n - 1
        else:  # normal case
            pos = (L + R) // 2
        # print(L, pos, R, -(pos-L)//2, -(R-pos)//2)
        heapq.heappush(self.seats, (-((pos - L) // 2), L, pos))
        heapq.heappush(self.seats, (-((R - pos) // 2), pos, R))
        return pos

    # TC:O(N), SC:O(N)
    def leave(self, p: int) -> None:
        # find interval with p, and delete it
        head = tail = None
        seats = []
        for d, L, R in self.seats:
            if L == p:
                tail = R
            elif R == p:
                head = L
            else:
                seats.append((d, L, R))
        seats.append((-(tail - head) // 2, head, tail))
        heapq.heapify(seats)
        self.seats = seats

# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)