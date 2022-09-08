# https://leetcode.com/problems/median-of-two-sorted-arrays/
# https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2471/Very-concise-O(log(min(MN)))-iterative-solution-with-detailed-explanation


# TC:O(log(min(n,m))), SC: O(1)
def findMedianSortedArrays(nums1, nums2) -> float:
    if len(nums2) > len(nums1):
        # make nums1 is a larger array
        return findMedianSortedArrays(nums2, nums1)
    # test 1,3,5,7,9(5) and 2,5(2) => (pos1,pos2) i_target=3 => (4,1) => (2,1)
    n = len(nums1)  # longer
    m = len(nums2)  # shorter
    L, R = 0, m - 1
    while True:
        mid2 = (L + R) // 2  # shorter, partition shorter array
        mid1 = (n + m) // 2 - mid2 - 2  # longer

        # print(mid1, mid2, n, m, L, R)
        num_L1 = nums1[mid1] if mid1 >= 0 else float("-inf")
        num_R1 = nums1[mid1 + 1] if mid1 + 1 < n else float("inf")
        num_L2 = nums2[mid2] if mid2 >= 0 else float("-inf")
        num_R2 = nums2[mid2 + 1] if mid2 + 1 < m else float("inf")

        if num_L1 <= num_R2 and num_L2 <= num_R1:
            return min(num_R1, num_R2) if (n + m) & 1 else (max(num_L1, num_L2) + min(num_R1, num_R2)) / 2
        elif num_L2 > num_R1:  # partition shorter array become shorter
            # move R to left
            R = mid2 - 1
        else:
            L = mid2 + 1



# TC:O(log(min(n,m))), SC: O(1)
def findMedianSortedArrays2(nums1, nums2) -> float:
    N1, N2 = len(nums1), len(nums2)
    if N1 < N2:
        nums1, N1, nums2, N2 = nums2, N2, nums1, N1
    l, r = 0, N2*2
    while l <= r:
        j = (l + r) >> 1
        i = N1 + N2 - j
        L1 = float("-inf") if i == 0 else nums1[(i-1)>>1]
        L2 = float("-inf") if j == 0 else nums2[(j-1)>>1]
        R1 = float("inf") if i == 2*N1 else nums1[i>>1]
        R2 = float("inf") if j == 2*N2 else nums2[j>>1]
        if L1 > R2: l = j + 1
        elif L2 > R1: r = j - 1
        else:
            return (max(L1, L2) + min(R1, R2))/2.0





# trick to handle edge cases, TC:O(log(min(n,m))), SC: O(1)
def findMedianSortedArrays3(nums1, nums2) -> float:
    n1, n2 = len(nums1), len(nums2)
    if n1 < n2: return findMedianSortedArrays3(nums2, nums1)
    nums1 += [float('inf'), float('-inf')]
    nums2 += [float('inf'), float('-inf')]
    left, right = 0, 2 * n2
    while left <= right:
        mid2 = left + (right - left) // 2
        mid1 = n1 + n2 - mid2
        L1, R1 = nums1[(mid1 - 1) // 2], nums1[mid1 // 2]
        L2, R2 = nums2[(mid2 - 1) // 2], nums2[mid2 // 2]
        if L1 > R2:
            left = mid2 + 1
        elif L2 > R1:
            right = mid2 - 1
        else:
            return (max(L1, L2) + min(R1, R2)) / 2


