# https://leetcode.com/problems/shuffle-the-array/description/
# https://leetcode.com/problems/shuffle-the-array/solutions/675956/in-place-o-n-time-o-1-space-with-explanation-analysis/


# in-place solution, TC:O(N), SC:O(1)
def shuffle(nums: List[int], n: int) -> List[int]:
    # max 1000 => 2^10
    for i in range(n):
        nums[i + n] = nums[i + n] << 10 | nums[i]  # store all num into n ~ 2n

    bit_mask = (1 << 10) - 1  # 01111111111

    for i in range(n):
        nums[2 * i] = nums[i + n] & bit_mask
        nums[2 * i + 1] = (nums[i + n] >> 10) & bit_mask
    return nums
