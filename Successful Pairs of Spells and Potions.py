# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/



# binary search, TC:O((N+M)logN), SC:O(N) for sorting
def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    def bsearch(nums, target):
        L, R = 0, len(nums) - 1
        while L <= R:
            mid = (L + R) // 2
            if nums[mid] >= target:
                R = mid - 1
            else:
                L = mid + 1
        return L

    potions.sort() # NlogN
    n = len(spells)
    res = [0] * n
    for i in range(n): # MlogN
        idx = bsearch(potions, success / spells[i])
        res[i] = len(potions) - idx
    return res