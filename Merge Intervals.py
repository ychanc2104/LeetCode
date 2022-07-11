


def merge(intervals):
    # intervals.sort()
    intervals = sorted(intervals, key=lambda x:x[0])
    res = [intervals[0]]
    for interval in intervals[1:]:
        r = res[-1]
        if r[0] <= interval[0] <= r[1]:
            interval[0] = r[0]
            if r[1] > interval[1]:
                interval[1] = r[1]
            res[-1] = interval
        else:
            res.append(interval)
    return res


def merge2(intervals):
    out = []
    for num in sorted(intervals, key=lambda x: x[0]):
        if out and num[0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], num[1])
        else:
            out.append(num)
    return out

def merge3(intervals):
    intervals = sorted(intervals, key=lambda x:x[0])
    res = [intervals[0]]
    for interval in intervals[1:]:
        if interval[0] <= res[-1][1]:
            ## no need to change start because array if sorted
            # use max to replace if statement
            res[-1][1] = max(res[-1][1], interval[1])
        else:
            res.append(interval)
    return res

# TC:O(nlogn) for sorting, SC:O(n) for timsort
def merge4(intervals):
    intervals.sort()
    res = [intervals[0]]
    for i in range(1,len(intervals)):
        if intervals[i][0] <= res[-1][1]:
            # overlapping
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])
    return res

intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]


res = merge(intervals)

res2 = merge2(intervals)

res3 = merge3(intervals)
