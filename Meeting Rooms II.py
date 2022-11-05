# https://leetcode.com/problems/meeting-rooms-ii/
# https://leetcode.com/problems/meeting-rooms-ii/discuss/67860/My-Python-Solution-With-Explanation
# https://leetcode.com/problems/meeting-rooms-ii/discuss/67917/Python-heap-solution-with-comments.
# https://leetcode.com/problems/meeting-rooms-ii/discuss/272822/Python-Greedy-Interval-Partition-Problem


import heapq

# first thought, TC:O(nlogn+n^2), SC:O(n)
def minMeetingRooms(intervals) -> int:
    intervals.sort()
    # print(intervals)
    res = []
    # TC:O(1+2+3+...+n) = O(n^2) for worst case
    for start, end in intervals:
        if not res:
            res.append([start, end])
            continue
        n = len(res)
        for i in range(n):
            # once not overlapping, directly connect to this room
            if not (res[i][0] <= start < res[i][1]):
                res[i][1] = max(res[i][1], end)
                break
            elif i == n - 1:
                # overlapping and no room can be compared
                res.append([start, end])
    # print(i, res)
    return len(res)

# greedy, TC:O(nlogn), SC:O(n)
def minMeetingRooms2(intervals) -> int:
    # if overlapping => add one room
    starts = sorted([s for s, e in intervals])
    ends = sorted([e for s, e in intervals])

    res = count = 0
    i_s = i_e = 0
    while i_s < len(starts):
        if starts[i_s] < ends[i_e]:
            # add one room
            count += 1
            i_s += 1
            res = max(res, count)
        else:
            i_e += 1
            count -= 1
    return res

# concise greedy, TC:O(nlogn), SC:O(n)
def minMeetingRooms3(intervals) -> int:    # if overlapping => add one room
    starts = sorted([s for s, e in intervals])
    ends = sorted([e for s, e in intervals])
    res = 0
    i_e = 0
    for s in starts:
        if s < ends[i_e]:
            # add one room
            res += 1
        else:
            i_e += 1
    return res


# priority queues, TC:O(nlogn), SC:O(n)
def minMeetingRooms4(intervals) -> int:    # if overlapping => add one room
    # if overlapping => add one room
    intervals.sort()
    # create min heap to store end time
    rooms = []
    for s,e in intervals:
        if rooms and s >= rooms[0]:
            # means two intervals can use the same room
            heapq.heapreplace(rooms, e)
            # no need one room
            # heapq.heappop(rooms)
            # heapq.heappush(rooms, e)
        else:
            # a new room is allocated
            heapq.heappush(rooms, e)

    return len(rooms)


# greedy, TC:O(nlogn), SC:O(n)
def minMeetingRooms5(intervals) -> int:
    # 0,5,15
    # 10,20,30
    start = sorted([s for s,e in intervals])
    end = sorted([e for s,e in intervals])
    res = 0
    i, j = 0, 0
    while i < len(start):
        if start[i] >= end[j]: # not overlapping, remove a room
            res -= 1
            j += 1
        i += 1
        res += 1
    return res