# https://leetcode.com/problems/design-hit-counter/
# https://leetcode.com/problems/design-hit-counter/discuss/121033/Follow-up-on-Hit-Counter-on-largepeak-data-streams


# first thought, binary search
class HitCounter:

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    # TC:O(logN)
    def getHits(self, timestamp: int) -> int:
        # rightmost binary search to find delete portion or linear search to delete
        # not including target
        target = timestamp - 300
        L, R = 0, len(self.hits)-1
        while L <= R:
            mid = L + (R-L)//2
            if self.hits[mid] > target:
                # move R to mid-1
                R = mid - 1
            else:
                L = mid + 1
        # return len(self.hits[R+1:])
        return len(self.hits) - (R + 1)

# first thought, binary search, maintain size of hits <= 300
class HitCounter2:

    def __init__(self):
        self.hits = collections.deque([])

    def hit(self, timestamp: int) -> None:
        while len(self.hits) >= 300:
            self.hits.popleft()
        else:
            self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # rightmost binary search to find delete portion or linear search to delete
        # not including target
        target = timestamp - 300
        L, R = 0, len(self.hits) - 1
        while L <= R:
            mid = L + (R - L) // 2
            if self.hits[mid] > target:
                # move R to mid-1
                R = mid - 1
            else:
                L = mid + 1

        return len(self.hits) - R - 1