# https://leetcode.com/problems/shortest-word-distance-ii/

import collections

# first thought
class WordDistance:
    # TC:O(N), SC:O(N)
    def __init__(self, wordsDict: list[str]):
        self.memo = collections.defaultdict(list)
        for i, s in enumerate(wordsDict):
            self.memo[s].append(i)

    # TC:O(kM)
    def shortest(self, word1: str, word2: str) -> int:
        return min(abs(i - j) for i in self.memo[word1] for j in self.memo[word2])


class WordDistance2:

    def __init__(self, wordsDict: List[str]):
        self.memo = collections.defaultdict(list)
        for i, s in enumerate(wordsDict):
            self.memo[s].append(i)

    # TC:O(M+k)
    def shortest(self, word1: str, word2: str) -> int:
        # [1,3,5] and [6,7,9]
        l1, l2 = self.memo[word1], self.memo[word2]
        n1, n2 = len(l1), len(l2)
        i, j = 0, 0
        res = float('inf')
        while i < n1 and j < n2:
            res = min(res, abs(l1[i] - l2[j]))
            if l1[i] > l2[j]:
                j += 1
            else:
                i += 1
        return res



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)