# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/description/
# https://leetcode.com/problems/removing-minimum-number-of-magic-beans/solutions/1766764/c-java-python3-sorting-4-lines/

# TC:O(nlogn), SC:O(n)
def minimumRemoval(beans: List[int]) -> int:
    # make all other elements to be same with beans[i]
    # res[i] = beans[0]+beans[1]+...+beans[i-1] + (beans[i+1]-beans[i]) + (beans[i+2]-beans[i]) + (beans[n-1]-beans[i]) = sum(beans) - beans[i] * (n-i)
    beans.sort()  # TC:O(nlogn), SC:O(n)
    s = sum(beans)
    res = s
    for i in range(len(beans)):
        res = min(res, s - beans[i] * (len(beans) - i))  # select i as pivot
    return res