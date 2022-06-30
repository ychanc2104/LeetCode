# https://leetcode.com/problems/insert-interval/
# https://leetcode.com/problems/insert-interval/discuss/844494/Python-O(n)-solution-explained

# separate into (left + newInterval + right)

## T: O(nlogn)
def insert(intervals, newInterval):
    intervals.append(newInterval)
    intervals = sorted(intervals, key=lambda x :x[0])
    res = [intervals[0]]
    for num in intervals:
        if res[-1][1 ]>=num[0]:
            res[-1][1] = max(res[-1][1], num[1])
        else:
            res.append(num)
    return res

## T:O(n)
def insert2(intervals, newInterval):
    I = [newInterval]
    res = []
    for num in intervals:
        if I:
            ## overlapping with I
            if not ((num[1] < I[0][0]) or (num[0] > I[0][1])):
                # print('overlapping')
                # update I
                I[0] = [min(I[0][0], num[0]), max(I[0][1], num[1])]
            ## not overlapping
            else:
                # check small or bigger than num[0]
                if I[0][0] < num[0]:
                    res.append(I[0])
                    I.pop()
                    res.append(num)
                else:
                    res.append(num)
        else:  #
            res.append(num)
    if I:
        res.append(I[0])
    return res


## T:O(n)
def insert3(intervals, newInterval):
    left = []
    k = 0

    for num in intervals:
        ## overlapping, merge
        if not (num[0] > newInterval[1] or num[1] < newInterval[0]):
            newInterval = [min(newInterval[0], num[0]), max(newInterval[1], num[1])]
            k += 1
        ## non-overlapping
        else:
            # left case
            if num[0] < newInterval[0]:
                left.append(num)
                k += 1
    return left + [newInterval] + intervals[k:]

## T:O(n)
def insert4(intervals, I):
    res, i = [], -1
    for i, (x, y) in enumerate(intervals):
        if y < I[0]:
            res.append([x, y])
        elif I[1] < x:
            i -= 1
            break
        else:
            I[0] = min(I[0], x)
            I[1] = max(I[1], y)
    return res + [I] + intervals[i + 1:]

## T:O(n), SC:O(1)
def insert5(intervals, newInterval):
    res = []
    L, R = newInterval
    isInsert = False
    for s, e in intervals:
        if s <= L <= e or s <= R <= e or (L <= s and R >= e):
            # overlapping
            L, R = min(s, L), max(e, R)
        else:
            # not overlapping
            if not isInsert and s > L:
                res.append([L, R])
                isInsert = True
            res.append([s, e])
    # edge case for len(intervals)<=1
    if not isInsert:
        res.append([L, R])
    return res


## T:O(n), SC:O(1)
def insert6(intervals, newInterval):
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

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]

newInterval = [4,8]

# res = insert(intervals, newInterval)

res2 = insert2(intervals, newInterval)