# https://leetcode.com/problems/my-calendar-iii/description/
# https://leetcode.com/problems/my-calendar-iii/solutions/2670758/leetcode-the-hard-way-explained-line-by-line/?orderBy=most_votes&languageTags=python

from collections import Counter
from sortedcontainers import SortedDict
from itertools import accumulate


# first thought, return Max number of overlapping intervals, TC:O(n^2*logn) for total n calls
class MyCalendarThree:

    def __init__(self):
        self.intervals = []
    # TC:O(nlogn+2n) for each call, SC:O(n)
    def book(self, start: int, end: int) -> int:
        self.intervals.append([start, end])
        # find max overlapping interval
        starts = sorted([s for s, e in self.intervals])
        ends = sorted([e for s, e in self.intervals])
        res = 0
        temp = 0
        i = 0
        for s in starts:
            # print(s,ends[i])
            while ends[i] <= s:
                i += 1
                temp -= 1
            else:
                # overlapping
                temp += 1
                res = max(res, temp)
        return res


class MyCalendarThree:

    def __init__(self):
        self.intervals = []
    # TC:O(nlogn+2n) for each call, O(), SC:O(n)
    def book(self, start: int, end: int) -> int:
        self.intervals.append([start, end])
        # find max overlapping interval
        starts = sorted([s for s,e in self.intervals])
        ends = sorted([e for s,e in self.intervals])
        res = 0
        temp = 0
        i_s, i_e = 0, 0
        while i_s < len(starts):
            if ends[i_e] <= starts[i_s]:
                i_e += 1
                temp -= 1
            else:
                # overlapping, try next starts
                i_s += 1
                temp += 1
                res = max(res, temp)
        return res



# Time Complexity: O(N ^ 2)
# Space Complexity: O(N)
class MyCalendarThree:

    def __init__(self):
        self.diff = SortedDict()

    def book(self, start: int, end: int) -> int:
        self.diff[start] = self.diff.get(start, 0) + 1
        self.diff[end] = self.diff.get(end, 0) - 1
        cur = res = 0
        for delta in self.diff.values():
            cur += delta
            res = max(cur, res)
        return res

# Time Complexity: O(N ^ 2)
# Space Complexity: O(N)
class MyCalendarThree:

    def __init__(self):
        # in line sweeping, we need to ensure the keys are sorted
        # in python, we can use SortedDict which fulfils the above requirement
        # lines[i] = j means we have j overlapping elements at time point i
        self.lines = SortedDict()


    # finding number of overlapping elements at time points -> line sweeping
    def book(self, start: int, end: int) -> int:
        # new event starts here -> increase by 1
        self.lines[start] = self.lines.get(start, 0) + 1
        # the event ends here -> decrease by 1
        # p.s. sometimes you may see `lines.get(end + 1, 0) - 1;`. e.g. 2406. Divide Intervals Into Minimum Number of Groups
        #      you may search `leetcode-the-hard-way` on Discussion to see my solution explanation on that problem
        #      this is because the interval is inclusive, i.e [start, end]
        #      however, the interval in this problem is [start, end), so we don't need to add 1 here.
        self.lines[end] = self.lines.get(end, 0) - 1
        # here we calculate the prefix sum using `accumulate`
        # and get the maximum overlapping intervals using `max`
        return max(accumulate(self.lines.values()))





# TC:O(NlogC), C is max time ~10^9 in the problem, SC:O(NlogC) logC is number of recursive call
class MyCalendarThree:

    def __init__(self):
        self.vals = Counter()
        self.lazy = Counter()

    def update(self, start: int, end: int, left: int = 0, right: int = 10**9, idx: int = 1) -> None:
        if start > right or end < left:
            return

        if start <= left <= right <= end:
            self.vals[idx] += 1
            self.lazy[idx] += 1
        else:
            mid = (left + right)//2
            self.update(start, end, left, mid, idx*2)
            self.update(start, end, mid+1, right, idx*2 + 1)
            self.vals[idx] = self.lazy[idx] + \
                max(self.vals[2*idx], self.vals[2*idx+1])

    def book(self, start: int, end: int) -> int:
        self.update(start, end-1)
        return self.vals[1]


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)