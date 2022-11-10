
import collections

# range min query
# build tree, TC:O(N)
def createTree(low, high, pos):
    if low == high:
        tree[pos] = nums[low]
        return
    mid = (low + high) // 2
    # print(low, high, mid, pos)
    createTree(low, mid, 2 * pos + 1) # go left
    createTree(mid+1, high, 2 * pos + 2) # go right
    tree[pos] = min(tree[2*pos+1], tree[2*pos+2]) # min of left and right

# query, TC:O(logN)
def rangeQuery(qlow, qhigh, low, high, pos=0): # start from index 0
    # no overlapping
    if high < qlow or low > qhigh:
        return float("inf")
    # total overlapping
    if qlow <= low <= high <= qhigh:
        return tree[pos]
    # other cases => search left and right
    mid = (low + high) // 2
    L = rangeQuery(qlow, qhigh, low, mid, 2 * pos + 1)
    R = rangeQuery(qlow, qhigh, mid + 1, high, 2 * pos + 2)
    return min(L, R)




nums = [-1, 0, 3, 6, -5]
# tree = collections.defaultdict(int)
tree = [float("inf")] * (2*len(nums) - 1)

createTree(0, len(nums)-1, 0)

a1 = rangeQuery(1, 4, 0, len(nums)-1, 0)