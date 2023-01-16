# https://leetcode.com/problems/insert-interval/
# https://leetcode.com/problems/insert-interval/discuss/844494/Python-O(n)-solution-explained

# separate into (left + newInterval + right)

## T:O(n), SC:O(N)
def insert(intervals, newInterval):
    ## separate into three parts, left + merged newInterval + rest of intervals, put overlapping case to the 'else'
    res = []
    i = 0
    for s, e in intervals:
        if e < newInterval[0]:
            # non-overlapping but smaller
            res.append([s, e])
        elif newInterval[1] < s:
            # exceed
            break
        else:
            # overlapping
            newInterval[0] = min(newInterval[0], s)
            newInterval[1] = max(newInterval[1], e)
        i += 1
    return res + [newInterval] + intervals[i:]


## T:O(n), SC:O(1)
def insert2(intervals, newInterval):
    ## separate into three parts, left + merged newInterval + rest of intervals, put overlapping case to the 'else'
    k = 0
    i = 0
    for s,e in intervals:
        if e < newInterval[0]:
            # left
            k += 1
        elif s > newInterval[1]:
            break
        else:
            # overlapping
            newInterval = [min(s, newInterval[0]), max(e, newInterval[1])]
        i += 1
    return intervals[:k] + [newInterval] + intervals[i:]

def insert3(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    j = 0
    k = len(intervals)
    for i,(s,e) in enumerate(intervals):
        if e < newInterval[0]: # smaller than inserted
            j += 1 # move pointer
        elif s <= newInterval[1]: # overlapping
            newInterval = [min(newInterval[0], s), max(newInterval[1], e)]
        else: # non-overlapping
            k = i
            break
    return intervals[:j] + [newInterval] + intervals[k:]


intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]

newInterval = [4,8]

# res = insert(intervals, newInterval)

res2 = insert2(intervals, newInterval)