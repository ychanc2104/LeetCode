# https://leetcode.com/problems/arithmetic-subarrays/
# https://leetcode.com/problems/arithmetic-subarrays/solutions/909120/python3-using-set-no-sort-o-mn/?orderBy=most_votes

# use math and set without sorting, TC:O(NM) N is length of nums, M is length of l, SC:O(N)
def checkArithmeticSubarrays(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    def check(arr):  # TC:O(N), SC:O(N)
        n = len(arr)
        m, M = min(arr), max(arr)
        d = (M - m) // (n - 1)
        if M - m == 0:
            return True
        elif M - m < n - 1:
            return False
        memo = set([m + d * i for i in range(n)])
        for num in arr:
            if num not in memo:
                return False
            memo.remove(num)
        return True

    res = []
    for i, j in zip(l, r): # TC:O(NM)
        res.append(check(nums[i:j + 1]))
    return res

# use math and set without sorting, TC:O(NM) N is length of nums, M is length of l, SC:O(N)
def checkArithmeticSubarrays2(nums: List[int], l: List[int], r: List[int]) -> List[bool]:
    def check(arr): # TC:O(N), SC:O(N)
        n = len(arr)
        arr_set = set(arr)
        if n!=len(arr_set):
            return len(arr_set)==1 # no duplicates below
        m, M = min(arr), max(arr)
        d = (M-m) // (n-1)
        memo = set([m+d*i for i in range(n)])
        for num in range(m, M+1, d):
            if num not in arr_set:
                return False
        return True
    res = []
    for i,j in zip(l, r):
        res.append(check(nums[i:j+1]))
    return res