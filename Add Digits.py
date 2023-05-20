# https://leetcode.com/problems/add-digits/description/

# math, TC:O(1), SC:O(1)
def addDigits(num: int) -> int:
    # 0~9
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    return num % 9