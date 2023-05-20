# https://leetcode.com/problems/sliding-subarray-beauty/description/
# https://leetcode.com/problems/sliding-subarray-beauty/solutions/3445659/c-java-python3-simple-counting/

# bucket sort, TC:O(N), SC:O(1)
def getSubarrayBeauty(nums: List[int], k: int, x: int) -> List[int]:
    n = len(nums)
    counter = [0] * 101
    for i in range(k - 1):
        if nums[i] < 0:
            counter[nums[i] + 50] += 1
    res = [0] * (n - k + 1)
    for i in range(k - 1, n):
        counter[nums[i] + 50] += 1
        s = 0
        for j in range(50):
            s += counter[j]
            if s >= x:
                res[i - k + 1] = j - 50
                break
        # print(i, k, nums[i-k+1])
        counter[nums[i - k + 1] + 50] -= 1
    return res