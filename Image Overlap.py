# https://leetcode.com/problems/image-overlap/description/
# https://leetcode.com/problems/image-overlap/solutions/130623/c-java-python-straight-forward/

import collections


# TC:O(N^2), SC:O(N^2)
def largestOverlap(img1: List[List[int]], img2: List[List[int]]) -> int:
    # find same transform vector, (xi-xj, yi-yj), return max count is the max overlapping area
    # n = len(img1)
    non_zero1 = [(i, j) for i in range(len(img1)) for j in range(len(img1[0])) if img1[i][j] != 0]
    non_zero2 = [(i, j) for i in range(len(img2)) for j in range(len(img2[0])) if img2[i][j] != 0]
    counter = collections.Counter((xi - xj, yi - yj) for (xi, yi) in non_zero1 for (xj, yj) in non_zero2)
    return max(counter.values()) if len(counter) != 0 else 0