# https://leetcode.com/problems/majority-element/
# https://leetcode.com/problems/majority-element/discuss/51613/O(n)-time-O(1)-space-fastest-solution
# https://leetcode.com/problems/majority-element/discuss/543431/Majority-vote-algorithm-EXPLAINED-(with-pictures)
# Boyer–Moore string-search algorithm

# first thought, TC:O(n), SC:O(n)
def majorityElement(nums) -> int:
    counter = {}
    for n in nums:
        counter[n] = counter.get(n, 0) + 1
        if counter[n] > len(nums) // 2:
            return n

# TC:O(n), SC:O(1)
def majorityElement2(nums) -> int:
    res = nums[0]
    counter = 1
    for n in nums[1:]:
        if counter>len(nums)//2:
            break
        elif res==n:
            counter += 1
        elif counter==0:
            res = n
            counter = 1
        elif res!=n:
            counter -= 1
    return res

# TC:O(n), SC:O(1), Boyer–Moore string-search algorithm
def majorityElement3(nums) -> int:
    res = nums[0]
    counter = 1
    for n in nums[1:]:
        if counter == 0:
            res = n
        counter += 1 if res == n else -1
    return res