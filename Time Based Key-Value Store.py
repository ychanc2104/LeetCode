# https://leetcode.com/problems/time-based-key-value-store/
# https://leetcode.com/problems/time-based-key-value-store/discuss/449517/Python-solution

import collections

#
class TimeMap:

    def __init__(self):
        # key store timestamp as values
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamps are strictly increasing
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # binary search
        arr = self.map[key]
        if not arr: return ""
        L, R = 0, len(arr)-1
        while L<R:
            # target: timestamp
            mid = L + (R-L)//2 # [L, R) never touch R
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                # to left
                R = mid - 1
            else:
                # find the rightmost
                # 1,3,4,7,8, target=6
                L = mid + 1
        # remaining element
        if arr[L][0]>timestamp:
            L -= 1
        return arr[L][1] if L>=0 else ""


class TimeMap2:

    def __init__(self):
        # key store timestamp as values
        self.map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamps are strictly increasing
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        # binary search
        arr = self.map[key]
        if not arr: return ""
        L, R = 0, len(arr)-1
        while L<R:
            # target: timestamp
            mid = L + (R-L+1)//2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] > timestamp:
                # to left
                R = mid - 1
            else:
                # find the rightmost
                # 1,3,4,7,8, target=6
                L = mid
        # remaining element
        return arr[L][1] if timestamp>=arr[L][0] else ""