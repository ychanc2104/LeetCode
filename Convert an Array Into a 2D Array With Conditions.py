# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/solutions/3368523/java-c-python-maximum-frequence/

# first thought, TC:O(N^2), SC:O(N)
def findMatrix(nums: List[int]) -> List[List[int]]:
    res = [[]]
    memo = [set()]
    for num in nums:
        for r in range(len(res)):
            if num not in memo[r]:
                res[r].append(num)
                memo[r].add(num)
                break
        else:  # cannot insert into existing row
            res.append([num])
            memo.append(set([num]))
    return res



# use counter, 1 <= nums[i] <= nums.length, TC:O(N), SC:O(N)
def findMatrix2(nums: List[int]) -> List[List[int]]:
    res = [[]]
    counter = [0] * (len(nums) + 1)
    for num in nums:
        if counter[num] >= len(res):
            res.append([])
        res[counter[num]].append(num)
        counter[num] += 1

    return res