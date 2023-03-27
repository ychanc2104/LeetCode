# https://leetcode.com/problems/reaching-points/


# brute force, TC:O(), SC:O()
def reachingPoints(sx: int, sy: int, tx: int, ty: int) -> bool:
    def helper(x, y):
        if x > tx or y > ty:
            return False
        if x == tx and y == ty:
            return True
        if helper(x + y, y) or helper(x, x + y):
            return True
        return False

    return helper(sx, sy)

# TC:O(max(tx, ty)), SC:O(1)
# every child only has one parent, (x, y) => parent (x-y, y) if x > y
# (x, y-x) for y > x
# find path from (tx,ty) to (sx,sy)
def reachingPoints2(sx: int, sy: int, tx: int, ty: int) -> bool:
    # every child only has one parent, (x, y) => parent (x-y, y) if x > y
    # (x, y-x) for y > x
    # find path from (tx,ty) to (sx,sy)
    while True:
        if tx == sx and ty == sy:
            return True
        elif tx < sx or ty < sy:
            return False
        if tx > ty:
            tx -= ty
        else:
            ty -= tx


# speed up subtraction by modulo TC:O(log(max(tx, ty))), SC:O(1)
# every child only has one parent, (x, y) => parent (x-y, y) if x > y
# (x, y-x) for y > x
# find path from (tx,ty) to (sx,sy)
def reachingPoints3(sx: int, sy: int, tx: int, ty: int) -> bool:
    # every child only has one parent, (x, y) => parent (x-y, y) if x > y
    # (x, y-x) for y > x
    # find path from (tx,ty) to (sx,sy)
    # speed up subtract using modulo
    while True:
        if tx == sx and ty == sy:
            return True
        elif tx < sx or ty < sy:
            return False
        if tx > ty:
            if sy==ty and tx%ty == sx%ty:
                return True
            tx %= ty
        else:
            if sx==tx and ty%tx == sy%tx:
                return True
            ty %= tx