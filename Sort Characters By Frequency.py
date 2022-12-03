# https://leetcode.com/problems/sort-characters-by-frequency/description/

import collections, heapq


# use heap, TC:O(N), SC:O(1) upper bound O(26)
def frequencySort(s: str) -> str:
    counter = collections.Counter(s) # TC:O(N), SC:O(1)
    res = []
    heap = [(-c, char) for char, c in counter.items()] # TC:O(1), SC:O(1)
    heapq.heapify(heap) # TC:O(1)
    while heap: # O(1)
        neg_count, char = heapq.heappop(heap)
        res.append(char * (-neg_count)) # TC:O(N) in total
    return ''.join(res)


# use bucket, TC:O(N), SC:O(N)
def frequencySort2(s: str) -> str:
    counter = collections.Counter(s) # TC:O(N), SC:O(1)
    M_count = max(counter.values()) # TC:O(1)
    bucket = [[] for _ in range(M_count+1)] # TC:O(N)
    # put into bucket
    for char,count in counter.items(): # TC:O(1)
        bucket[count].append(char) # SC:O(N)
    res = []
    # get res from max
    for i in range(M_count,0,-1): # TC:O(N) worst in total
        for c in bucket[i]:
            res.append(i*c)
    return ''.join(res)