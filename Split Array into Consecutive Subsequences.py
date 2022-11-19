# https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/solutions/589680/python-heap/

import collections, heapq

# heap, TC:O(NlogN), SC:O(N)
def isPossible(nums: List[int]) -> bool:
    tails = collections.defaultdict(list)
    for num in nums:
        if not tails[num - 1]:  # empty
            heapq.heappush(tails[num], 1)  # store length
        else:
            heapq.heappush(tails[num], heapq.heappop(tails[num - 1]) + 1)
    # check all remaining heaps
    for v in tails.values():
        if v and any(x < 3 for x in v):
            return False
    return True

# greedy, TC:O(N), SC:O(N)
def isPossible2(nums: List[int]) -> bool:
    counter = collections.Counter(nums)
    memo_end = collections.Counter()  # store the end of valid sub seq
    for num in nums:
        if counter[num] == 0: continue  # already in valid subseq
        counter[num] -= 1
        if memo_end[num - 1] > 0:  # first to decide add to existing subseq or not
            memo_end[num - 1] -= 1
            memo_end[num] += 1 # update end
        elif counter[num + 1] and counter[num + 2]:  # create new subseq and check length 3
            counter[num + 1] -= 1
            counter[num + 2] -= 1
            memo_end[num + 2] += 1  # new subseq and end with num+2
        else:
            return False
    # print(memo_end)
    return True