# https://leetcode.com/problems/guess-the-majority-in-a-hidden-array/description/


# """
# This is the ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
# class ArrayReader(object):
#	 # Compares 4 different elements in the array
#	 # return 4 if the values of the 4 elements are the same (0 or 1).
#	 # return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
#	 # return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
#    def query(self, a: int, b: int, c: int, d: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#

# TC:O(N), SC:O(N)
def guessMajority(reader: 'ArrayReader') -> int:
    # 2 to 0, nums[i] != nums[i+4]
    # val change =>
    # 2,0,2,2,4
    # 0,0
    # 0,0,0,0,0
    n = reader.length()
    # s = 1
    # flag = True # value of idx 4
    nums = [True] * reader.length()
    check = reader.query(1, 2, 3, 4)
    i = 1
    # TC:O(4)
    for a, b, c, d in ((0, 2, 3, 4), (0, 1, 3, 4), (0, 1, 2, 4), (0, 1, 2, 3)):
        # not choose i
        # if check == reader.query(a,b,c,d):
        nums[i] = check == reader.query(a, b, c, d)
        i += 1
    # TC:O(n-4), total TC:O(n)
    for i in range(5, n):
        check2 = reader.query(1, 2, 3, i)  # i<n-3
        if check == check2:
            nums[i] = nums[4]
        else:
            nums[i] = not nums[4]
        # check = check2

    s = 0
    for b in nums:
        s += 1 if b else -1
    # print(nums, s)
    if s == 0:
        return -1
    elif s > 0:
        return 0
    return nums.index(False)

# TC:O(N), SC:O(1)
def guessMajority2(reader: 'ArrayReader') -> int:

    n = reader.length()
    s = 1
    check = reader.query(1,2,3,4)
    idx_diff = -1 # diff with 0
    i = 1
    # TC:O(4)
    for a,b,c,d in ((0,2,3,4),(0,1,3,4),(0,1,2,4),(0,1,2,3)):
        # not choose i
        check2 = reader.query(a,b,c,d)
        if check == check2:
            s += 1
        else:
            s -= 1
            idx_diff = i
        i += 1

    # TC:O(n-4), total TC:O(n)
    for i in range(5,n):
        check3 = reader.query(1,2,3,i) # i<n-3
        if check2 == check3:
            s += 1
        else:
            s -= 1
            idx_diff = i
        # check = check2
    if s == 0:
        return -1
    return 0 if s > 0 else idx_diff