# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/

def countOdds(low: int, high: int) -> int:
    if low & 1 and high & 1:  # low and high are odd
        return (high - low) // 2 + 1  # 3-5
    elif not low & 1 and not high & 1:
        return (high - low) // 2  # 4-6
    else:
        return (high - low) // 2 + 1  # 3-6