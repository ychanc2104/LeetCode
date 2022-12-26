# https://leetcode.com/problems/longest-subsequence-with-limited-sum/description/


# TC:O(MN + NlogN), SC:O(N)
def answerQueries(nums: List[int], queries: List[int]) -> List[int]:
    #
    nums.sort()
    res = []
    for target in queries:
        s = 0
        LS = 0
        for i in range(len(nums)):
            s += nums[i]
            if s > target:
                break
            LS = max(LS, i + 1)
        res.append(LS)
    return res


# prefix sum + binary search, TC:O(MlogN + NlogN), SC:O(N)
def answerQueries2(nums: List[int], queries: List[int]) -> List[int]:
    # prefix sum + binary search
    nums.sort()
    prefix, s = [], 0
    for num in nums:
        s += num
        prefix.append(s)

    def bsearch(nums, target):
        L, R = 0, len(nums) - 1
        # print(L, R, nums)
        while L <= R:
            mid = (L + R) // 2
            # if nums[mid] == target:
            #     return mid + 1
            if nums[mid] > target:
                R = mid - 1
            else:
                L = mid + 1
        return L  # [0, len(nums)]

    res = []
    for target in queries:
        LS = bsearch(prefix, target)
        res.append(LS)
    return res