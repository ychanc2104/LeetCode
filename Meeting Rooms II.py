# https://leetcode.com/problems/meeting-rooms-ii/
# https://leetcode.com/problems/meeting-rooms-ii/discuss/67860/My-Python-Solution-With-Explanation

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