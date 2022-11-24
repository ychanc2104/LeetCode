# https://leetcode.com/problems/magnetic-force-between-two-balls/?envType=study-plan&id=binary-search-ii

# binary search, TC:O(NlogN + NlogM) M is max(position) - min(position), SC:O(1)
def maxDistance(position: List[int], m: int) -> int:
    def countBall(k):
        end = position[-1]
        prevPos = position[0]
        count = 2
        for i in range(1, len(position) - 1):
            diff = min(position[i] - prevPos, end - position[i])
            if diff >= k:  # can place ball
                count += 1
                prevPos = position[i]
        return count

    # (L,R,mid,count) (1,7,4,2) => (1,3,2,3) => (3,3,3,3)
    position.sort()  # TC:O(NlogN), SC:O(N)
    L, R = 1, position[-1] - position[0]  # answer should be in range [1, position[-1]-position[0]]
    # binary search on answer
    while L <= R:  # TC:O(logM) M: max(position)
        mid = (L + R) // 2
        if countBall(mid) >= m:  # increase L, too many balls
            L = mid + 1
        else:
            R = mid - 1
    return R

# binary search + early return, TC:O(NlogN + NlogM) M is max(position) - min(position), SC:O(1)
def maxDistance2(position: List[int], m: int) -> int:
    def checkBall(k):
        end = position[-1]
        prevPos = position[0]
        count = 2
        for i in range(1, len(position)-1):
            diff = min(position[i] - prevPos, end - position[i])
            if diff >= k: # can place ball
                count += 1
                prevPos = position[i]
            if count >= m: return True
        return count >= m
    # (L,R,mid,count) (1,7,4,2) => (1,3,2,3) => (3,3,3,3)
    position.sort() # TC:O(NlogN), SC:O(N)
    L, R = 1, position[-1]-position[0] # answer should be in range [1, position[-1]-position[0]]
    # binary search on answer
    while L <= R: # TC:O(logM) M: max(position)
        mid = (L + R) // 2
        if checkBall(mid): # increase L, too many balls
            L = mid + 1
        else:
            R = mid - 1
    return R