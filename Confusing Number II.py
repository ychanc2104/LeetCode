# https://leetcode.com/problems/confusing-number-ii/description/
# https://leetcode.com/problems/confusing-number-ii/solutions/408771/python-ugly-backtracking-solution/


# backtracking, TC:O(5^log10(N)) = O(N^log10(5)), there are log10(N) position to be filled, SC:O(logN)
def confusingNumberII(n: int) -> int:
    rotate = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
    res = 0

    def backtrack(origin, rotation, digit=10):  # current number
        nonlocal res
        if origin != rotation:
            res += 1

        for num in (0, 1, 6, 8, 9):
            if origin * 10 + num > n:
                break
            backtrack(origin * 10 + num, rotation + rotate[num] * digit, digit * 10)

    for num in (1, 6, 8, 9):
        backtrack(num, rotate[num])
    return res


# backtracking, TC:O(5^log10(N)) = O(N^log10(5)), there are log10(N) position to be filled, SC:O(logN)
def confusingNumberII2(n: int) -> int:
    rotate = {0:0, 1:1, 6:9, 8:8, 9:6}

    def backtrack(origin, rotation, digit=10): # current number
        res = 0
        if origin != rotation:
            res += 1
        for num in (0,1,6,8,9):
            if (origin*10 + num > n) or (num==0 and origin==0):
                continue
            res += backtrack(origin*10 + num, rotation + rotate[num]*digit, digit*10)
        return res

    return backtrack(0, 0, 1)