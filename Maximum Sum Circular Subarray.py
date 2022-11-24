# https://leetcode.com/problems/maximum-sum-circular-subarray/description/?envType=study-plan&id=dynamic-programming-i
# https://leetcode.com/problems/maximum-sum-circular-subarray/solutions/178422/one-pass/


# dp, TC:O(N), SC:O(1)
def maxSubarraySumCircular(nums: List[int]) -> int:
    # store min subarray and max subarray
    # res = max(sum(nums) - resMin, resMax) for all num > 0
    tempSumMax = tempSumMin = nums[0]
    resMax = resMin = nums[0]
    for i in range(1, len(nums)):
        tempSumMax = max(nums[i], tempSumMax + nums[i])
        tempSumMin = min(nums[i], tempSumMin + nums[i])
        resMax = max(resMax, tempSumMax)
        resMin = min(resMin, tempSumMin)
    # compare 1.subarray include head or end, 2. subarray in the middle (confirm resMax > 0)
    return max(sum(nums) - resMin, resMax) if resMax > 0 else resMax