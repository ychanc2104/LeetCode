# https://leetcode.com/problems/non-overlapping-intervals/
# https://leetcode.com/problems/non-overlapping-intervals/discuss/91713/Java%3A-Least-is-Most
# classic Greedy problem: Interval Scheduling, https://en.wikipedia.org/wiki/Interval_scheduling#Interval_Scheduling_Maximization

## TC: O(NlogN) in total
def eraseOverlapIntervals(intervals):
    # TC: O(NlogN)
    intervals.sort(key=lambda intervals: (intervals[0], intervals[1]))
    # the smallest
    preEnd = intervals[0][1]
    res = 0
    # TC: O(N)
    for start, end in intervals[1:]:
        # overlapping
        if start < preEnd:
            res += 1
            # choose end is leftmost
            preEnd = min(preEnd, end)
        else:
            preEnd = end
    return res


