# https://leetcode.com/problems/plus-one/description/

# first thought, TC:O(N), SC:O(N)
def plusOne(digits: List[int]) -> List[int]:
    carry = 1
    res = []
    while digits or carry:
        num = digits.pop() if digits else 0
        if num + carry == 10:
            res.append(0)
        else:
            res.append(num + carry)
            carry = 0
    return res[::-1]

# TC:O(N), SC:O(N)
def plusOne2(digits: List[int]) -> List[int]:
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] + carry == 10:
            digits[i] = 0
        else:
            digits[i] += carry
            carry = 0
    if carry:
        return [1] + digits
    return digits