# https://leetcode.com/problems/seat-reservation-manager/

import heapq

class SeatManager:

    # SC:O(N)
    def __init__(self, n: int):
        self.empty = [i+1 for i in range(n)] # heaps

    # TC:O(logN)
    def reserve(self) -> int: # smallest idx
        return heapq.heappop(self.empty)

    # TC:O(logN)
    def unreserve(self, seatNumber: int) -> None: #
        heapq.heappush(self.empty, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)