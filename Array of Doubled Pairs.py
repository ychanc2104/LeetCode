# https://leetcode.com/problems/array-of-doubled-pairs/description/

# two pointers, TC:O(NlogN), SC:O(N) for sort
def canReorderDoubled(arr: List[int]) -> bool:
    arr.sort(key=lambda x: [abs(x), x])
    # print(arr)
    R = 0
    dummy = 100001
    for L in range(len(arr)):
        if arr[L] == dummy:
            continue
        if R <= L:
            R = L + 1
        while R < len(arr) and 2 * arr[L] != arr[R]:
            R += 1
        if R == len(arr):
            return False
        arr[R] = dummy
    return True