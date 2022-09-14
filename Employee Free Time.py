# https://leetcode.com/problems/employee-free-time/

import heapq

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end

# TC:O(nlogn) for merging k sorted arrays, SC:O(1)
def employeeFreeTime(schedule: '[[Interval]]') -> '[Interval]':
    # merge k sorted arrays, TC:O(nlogk)
    intervals = sorted([i for x in schedule for i in x], key=lambda x: x.start)
    #print([[x.start, x.end] for x in intervals])
    # if overlapping => update max of end, if not => append into res
    s, e = intervals[0].start, intervals[0].end
    res = []
    for i in range(1, len(intervals)):
        # overlapping
        if intervals[i].start <= e or s <= intervals[i].start <= e:
            e = max(e, intervals[i].end)
        else:
            # non-overlapping
            res.append(Interval(e, intervals[i].start))
            s = intervals[i].start
            e = intervals[i].end
    return res


# TC:O(nlogn) for merging k sorted arrays, SC:O(1)
def employeeFreeTime2(schedule: '[[Interval]]') -> '[Interval]':
    # merge k sorted arrays, TC:O(nlogk)
    intervals = sorted([i for x in schedule for i in x], key=lambda x: x.start)
    # print([[x.start, x.end] for x in intervals])
    # if overlapping => update max of end, if not => append into res
    s, e = intervals[0].start, intervals[0].end
    res = []
    for i in range(1, len(intervals)):
        if e < intervals[i].start:
            res.append(Interval(e, intervals[i].start))
        e = max(e, intervals[i].end)
    return res

# TC:O(nlogk) for merging k sorted arrays, SC:O(1)
def employeeFreeTime3(schedule: '[[Interval]]') -> '[Interval]':
    # merge k sorted arrays, TC:O(nlogk)
    compared_list = [(interval[0].start, i, 0) for i, interval in enumerate(schedule)]
    print(compared_list)
    heapq.heapify(compared_list)
    intervals = []
    while compared_list[0][0] != float("inf"):
        s, i, j = heapq.heappop(compared_list)
        intervals.append(schedule[i][j])
        if j + 1 >= len(schedule[i]):
            heapq.heappush(compared_list, (float("inf"), i, j + 1))
        else:
            heapq.heappush(compared_list, (schedule[i][j + 1].start, i, j + 1))

    # intervals = sorted([i for x in schedule for i in x], key=lambda x: x.start)
    # print([[x.start, x.end] for x in intervals])
    # if overlapping => update max of end, if not => append into res
    s, e = intervals[0].start, intervals[0].end
    res = []
    for i in range(1, len(intervals)):
        if e < intervals[i].start:
            res.append(Interval(e, intervals[i].start))
        e = max(e, intervals[i].end)
    return res