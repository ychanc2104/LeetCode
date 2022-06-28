# https://leetcode.com/problems/meeting-rooms/


# first thought, TC:O(nlogn), SC:O(1)
def canAttendMeetings( intervals) -> bool:
    if not intervals:
        return True
    intervals.sort()
    start, end = intervals[0]
    for s, e in intervals[1:]:
        if start <= s < end:
            # overlapping
            return False
        start, end = s, e
    return True

# clean version, TC:O(nlogn), SC:O(1)
def canAttendMeetings2(intervals) -> bool:
    intervals.sort()
    for i in range(len(intervals) - 1):
        # sorting has guaranteed intervals[i][0] <= intervals[i+1][0]
        if intervals[i + 1][0] < intervals[i][1]:
            # overlapping
            return False
    return True