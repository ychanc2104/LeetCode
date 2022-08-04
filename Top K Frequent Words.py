# https://leetcode.com/problems/top-k-frequent-words/
# https://leetcode.com/problems/top-k-frequent-words/discuss/431008/Summary-of-all-the-methods-you-can-imagine-of-this-problem
# https://leetcode.com/problems/top-k-frequent-words/discuss/108348/Python-3-solution-with-O(nlogk)-and-O(n)

import collections, heapq

# TC:O(nlogn), worst case all words in a same bucket, TC:O(n)
def topKFrequent(words, k: int):
    # bucket sort
    bucket = {i: [] for i in range(len(words) + 1)}
    # TC:O(n)
    counter = collections.Counter(words)
    # TC:O(n)
    for word, v in counter.items():
        bucket[v].append(word)
    # print(bucket, counter)
    count = 0
    res = []
    n = len(words)
    # worst O(nlogn), all words in a bucket
    while count < k:
        if bucket[n]:
            res.extend(sorted(bucket[n]))
            count += len(bucket[n])
        n -= 1
    return res[:k]


# min heap, TC:O(nlogk), TC:O(n)
def topKFrequent2(words, k: int):
    # SC: O(n)
    counter = {}
    for word in words:
        counter[word] = counter.get(word, 0) + 1
    #print(counter)
    freqs = []
    # TC:O(nlogk)
    for word, c in counter.items():
        # TC:O(logk)
        heapq.heappush(freqs, Pair(c, word))
        if len(freqs) > k:
            # pop out min
            heapq.heappop(freqs)
    return [heapq.heappop(freqs).word for _ in range(k)][::-1]

class Pair:
    def __init__(self, count, word):
        self.count = count
        self.word = word
    def __lt__(self, other):
        # <
        if self.count==other.count:
            return self.word > other.word
        else:
            return self.count < other.count

a = Pair(2, 'abc')
b = Pair(1, 'aac')
c = Pair(2, 'aac')
a<b