# https://leetcode.com/problems/find-the-index-of-the-large-integer/description/

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


# binary search, TC:O(logN), SC:O(1)
def getIndex(reader: 'ArrayReader') -> int:
    # (L,R,mid), (0,2,1)
    n = reader.length()
    L, R = 0, n - 1
    while L < R:
        mid = (L + R) // 2  # isolate mid if R-L is even

        if (L + R) % 2 == 0:
            check = reader.compareSub(L, mid - 1, mid + 1, R)  # prevent over-called
            if check == 1:
                R = mid - 1
            elif check == -1:
                L = mid + 1
            else:
                return mid
        else:  # equally separated
            check = reader.compareSub(L, mid, mid + 1, R)  # prevent over-called
            if check == 1:
                R = mid
            elif check == -1:
                L = mid + 1
    return L

# binary search, TC:O(logN), SC:O(1)
def getIndex2(reader: 'ArrayReader') -> int:
    # (L,R,mid), (0,2,1)
    n = reader.length()
    L, R = 0, n-1
    while L < R:
        mid = (L + R)//2 # isolate mid if R-L is even, 0,4 => 2 and 0,3 => 1
        mid2 = (L + R + 1)//2 # 0,4 => 2 and 0,3 => 2
        if (check:=reader.compareSub(L, mid, mid2, R)) == 1: # share the same mid if odd length
            R = mid
        elif check == -1:
            L = mid2
        else:
            return mid # shared num must be the large num
    return L