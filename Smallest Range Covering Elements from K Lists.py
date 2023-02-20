# https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

import heapq


# TC:O(nlogk) n is min length in nums and k is length of nums, SC: O(nk)
def smallestRange(nums):
    # merge k sorted lists
    # TC:O(k)
    compare_list = [(l[0], i, 0) for i, l in enumerate(nums)]
    # print(compare_list)
    # TC:O(k)
    heapq.heapify(compare_list)
    # TC:O(k)
    cur_max = max([l[0] for l in compare_list])
    res = [0, 0]
    diff = float('inf')
    # TC:O(nlogk)
    while compare_list[0][0] != float('inf'):
        cur_min, i, ii = heapq.heappop(compare_list)
        if cur_max - cur_min < diff:
            diff = cur_max - cur_min
            res = [cur_min, cur_max]
        if ii + 1 >= len(nums[i]):
            return res
        else:
            if nums[i][ii + 1] > cur_max:
                cur_max = nums[i][ii + 1]
            # TC:O(logk)
            heapq.heappush(compare_list, (nums[i][ii + 1], i, ii + 1))
    return res


# TC:O(nlogk) n is min length in nums and k is length of nums, SC: O(nk)
def smallestRange2(nums):
    compare = [(nums[k][0], k, 0) for k in range(len(nums))]
    heapq.heapify(compare)
    res = [min(compare, key=lambda x:x[0])[0], max(compare, key=lambda x:x[0])[0]]
    curMax = res[1]
    while True:
        num, k, i = heapq.heappop(compare)
        if i == len(nums[k])-1: # reach end
            break
        i += 1
        curMax = max(curMax, nums[k][i])
        heapq.heappush(compare, (nums[k][i], k, i))
        if res[1] - res[0] > curMax - compare[0][0]:
            res = [compare[0][0], curMax]
    return res