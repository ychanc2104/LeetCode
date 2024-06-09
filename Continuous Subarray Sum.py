# https://leetcode.com/problems/continuous-subarray-sum/description/?envType=daily-question&envId=2024-06-08

# TC:O(N), SC:O(N)
def checkSubarraySum(nums: List[int], k: int) -> bool:
    s = 0
    m = {0: -1}

    for i, num in enumerate(nums):
        s = (s + num) % k
        if s in m:
            if i - m[s] > 1:
                return True
        else:
            m[s] = i
    return False