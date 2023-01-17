# https://leetcode.com/problems/design-log-storage-system/

import collections


class LogSystem:

    def __init__(self):
        self.order = {"Year": 0, "Month": 1, "Day": 2, "Hour": 3, "Minute": 4, "Second": 5}
        self.memo = collections.defaultdict(list)  # ts:[IDs]

    # TC:O(1)
    def put(self, id: int, timestamp: str) -> None:
        self.memo[timestamp].append(id)

    # TC:O(N)
    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        # TC:O(1)
        def check(ts_list, start_list, end_list):
            ts, s, e = ''.join(ts_list), ''.join(start_list), ''.join(end_list)
            return s <= ts <= e

        start_list = start.split(':')[:self.order[granularity] + 1]
        end_list = end.split(':')[:self.order[granularity] + 1]
        res = []
        for ts, ids in self.memo.items():
            ts_list = ts.split(':')[:self.order[granularity] + 1]
            if check(ts_list, start_list, end_list):
                res.extend(ids)
        return res

# compare by tuple
class LogSystem2:

    def __init__(self):
        self.order = {"Year": 0, "Month": 1, "Day": 2, "Hour": 3, "Minute": 4, "Second": 5}
        self.memo = collections.defaultdict(list)  # ts:[IDs]

    def put(self, id: int, timestamp: str) -> None:
        self.memo[timestamp].append(id)

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        start_tuple = tuple(start.split(':')[:self.order[granularity] + 1])
        end_tuple = tuple(end.split(':')[:self.order[granularity] + 1])
        res = []
        for ts, ids in self.memo.items():
            ts_tuple = tuple(ts.split(':')[:self.order[granularity] + 1])
            if start_tuple <= ts_tuple <= end_tuple:
                res.extend(ids)
        return res

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)