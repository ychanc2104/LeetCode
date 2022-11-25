# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/?envType=study-plan&id=dynamic-programming-i
# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/solutions/819329/python3-go-java-dynamic-programming-o-n-time-o-1-space/

# space optimized dp, TC:O(N), SC:O(1)
def getMaxLen2(nums: List[int]) -> int:
    pos = res = 1 if nums[0] > 0 else 0  # previous longest positive product length (i-1)
    neg = 1 if nums[0] < 0 else 0  # previous longest negative product length (i-1)
    for i in range(1, len(nums)):
        if nums[i] < 0:  # neg = 1 or pos+1, pos = 0(neg==0) or neg + 1
            neg, pos = pos + 1, neg + 1 if neg > 0 else 0
        elif nums[i] == 0:
            neg = pos = 0
        elif nums[i] > 0:  # neg = 0(neg==0) or neg+1, pos = pos + 1
            neg, pos = neg + 1 if neg > 0 else 0, pos + 1
        res = max(res, pos)
    return res