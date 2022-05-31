# https://leetcode.com/problems/top-k-frequent-elements/
# https://leetcode.com/problems/top-k-frequent-elements/discuss/81631/3-ways-to-solve-this-problem
# https://leetcode.com/problems/top-k-frequent-elements/discuss/484980/Python-Explained-Two-Simple-Heap-solutions

## bucket sort
def topKFrequent(nums, k: int):
    # key:freq,    value:counter
    counter = {}
    # TC: O(n)
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    freq = [[] for i in range(len(nums) + 1)]
    # TC: O(n)
    for num, count in counter.items():
        freq[count].append(num)
    res = []
    # total TC: O(n) (two loops)
    for i in range(len(nums), -1, -1):
        buckets = freq[i]
        for v in buckets:
            res.append(v)
            if len(res) == k:
                return res


## heap, TC: O(nlogk)
def topKFrequent2(nums, k: int):
    if len(nums) == 1:
                return [nums[0]]

    # freq dict
    d = {}
    for num in nums:
        if num in d:
            d[num] += 1
        else:
            d[num] = 1

    # insert k items into heap O(nlog(k))
    h = []
    from heapq import heappush, heappop
    for key in d: # O(N)
        heappush(h, (d[key], key)) # freq, item - O(log(k))
        if len(h) > k:
            heappop(h)

    res = []
    while h: # O(k)
        frq, item = heappop(h) # O(logk)
        res.append(item)
    return res


nums = [1,1,1,2,2,3,4]
k = 2

res = topKFrequent(nums, k)

# check order of dict.items

a = {}
a[1] = 10
a[2] = 20
a[4] = 40
a[3] = 30
for v,k in a.items():
    print(v,k)