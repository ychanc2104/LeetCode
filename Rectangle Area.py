# https://leetcode.com/problems/rectangle-area/solutions/

# TC:O(1), SC:O(1)
def computeArea(ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
    xr = min(ax2, bx2)
    xl = max(ax1, bx1)
    yt = min(ay2, by2)
    yb = max(ay1, by1)

    area1 = (ax2 - ax1) * (ay2 - ay1)
    area2 = (bx2 - bx1) * (by2 - by1)
    area_int = (xr - xl) * (yt - yb)
    area_int = area_int if xr > xl and yt > yb else 0
    return area1 + area2 - area_int