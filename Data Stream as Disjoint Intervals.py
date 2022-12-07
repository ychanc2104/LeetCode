# https://leetcode.com/problems/data-stream-as-disjoint-intervals/
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/solutions/297728/short-python-union-find-solution/

class SummaryRanges:
    # union with value+1 and value-1, when addNum with same parent =>
    # make new intervals

    def __init__(self):
        self.parents = {}
        self.intervals = {}  # store interval of given parents

    def addNum(self, value: int) -> None:
        def find(x):
            if x not in self.parents: return -1
            if x != self.parents[x]:
                self.parents[x] = find(self.parents[x])
            return self.parents[x]

        def union(x, y):  # deal with interval
            px, py = find(x), find(y)
            if px == -1 or py == -1: return  # do nothing if not found its neighbor
            self.parents[px] = py
            # merge, x need to merge into existing neighbor
            m, M = self.intervals.pop(px)  # 2,2
            m2, M2 = self.intervals[py]  # 1,1 or 3,3
            self.intervals[py] = [min(m2, m), max(M2, M)]

        if value in self.parents: return  # do nothing
        # add to parents and intervals
        self.parents[value] = value
        self.intervals[value] = [value, value]
        # union with its neighbor if value and value-1 in self.parents
        union(value, value - 1)
        union(value, value + 1)

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.intervals.values())


class SummaryRanges2:
    # union with value+1 and value-1, when addNum with same parent =>
    # make new intervals

    def __init__(self):
        self.parents = {}
        self.intervals = {}  # store interval of given parents

    def addNum(self, value: int) -> None:
        def find(x):
            if x != self.parents[x]:
                self.parents[x] = find(self.parents[x])
            return self.parents[x]

        def union(x, y):  # deal with interval
            px, py = find(x), find(y)
            self.parents[px] = py
            # merge, x need to merge into existing neighbor
            m, M = self.intervals.pop(px)  # 2,2
            m2, M2 = self.intervals[py]  # 1,1 or 3,3
            self.intervals[py] = [min(m2, m), max(M2, M)]

        if value in self.parents: return  # do nothing
        # add to parents and intervals
        self.parents[value] = value
        self.intervals[value] = [value, value]
        # union with its neighbor if all parent in self.parents
        if value - 1 in self.parents:
            union(value, value - 1)
        if value + 1 in self.parents:
            union(value, value + 1)

    def getIntervals(self) -> List[List[int]]:
        return sorted(self.intervals.values())