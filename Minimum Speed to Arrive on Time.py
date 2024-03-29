# https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

# binary serach, TC:O(Nlogk) k is max speed, SC:O(1)
def minSpeedOnTime(dist: list[int], hour: float) -> int:
    def computeTime(speed):
        t = sum((dist[i] - 1) // speed + 1 for i in range(len(dist) - 1))
        # add float in the end to prevent float rounding error
        return t + dist[-1] / speed

    # (L,R,mid,t) 1,3,2,4 (move R)=> 1,1,1,6 (move R) => 0,1 stop
    max_speed = 10 ** 7  # upper bound
    L, R = 1, max_speed
    while L <= R:
        mid = (L + R) // 2
        if computeTime(mid) > hour:  # increase speed
            L = mid + 1
        else:
            R = mid - 1
    return L if L <= max_speed else -1


