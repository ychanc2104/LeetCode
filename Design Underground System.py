# https://leetcode.com/problems/design-underground-system/

import collections

# first thought
class UndergroundSystem:

    # TC:O(1), SC:O(N+M^2), N is number of people, M is number of stations
    def __init__(self):
        self.check_in = {} # (id: (station, t))
        self.travel = collections.defaultdict(int) # (start, end): total t
        self.sample = collections.defaultdict(int) # (start, end): count people

    # TC:O(1)
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = (stationName, t)

    # TC:O(1)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, t0 = self.check_in[id]
        self.travel[(start, stationName)] += t-t0
        self.sample[(start, stationName)] += 1

    # TC:O(1)
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.travel[(startStation, endStation)]/self.sample[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)