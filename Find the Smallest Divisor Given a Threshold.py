# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/?envType=study-plan&id=binary-search-ii


# binary search, TC:O(NlogM) M is max of nums, SC:O(1)
def smallestDivisor(self, nums: List[int], threshold: int) -> int:
    # (num-1)//d + 1
    def check(divisor):
        res = 0
        for num in nums:
            res += (num - 1) // divisor + 1
        return res <= threshold

    # try each divisor
    L, R = 1, max(nums) + 1
    while L <= R:
        divisor = (L + R) // 2
        if check(divisor):
            # move R
            R = divisor - 1
        else:
            L = divisor + 1
    return L