# https://leetcode.com/problems/shortest-word-distance-iii/description/


# first thought, two-pointers, TC:O(NM), M is len(word1), SC:O(1)
def shortestWordDistance(wordsDict: List[str], word1: str, word2: str) -> int:
    n = len(wordsDict)
    res = n
    if word1 == word2:
        j = -1
        for i in range(n):
            word = wordsDict[i]
            if word == word1:
                if j != -1:
                    res = min(res, i - j)
                j = i
    else:
        j, k = -1, -1
        for i in range(n):
            word = wordsDict[i]
            if word == word1:
                j = i
            elif word == word2:
                k = i
            if j != -1 and k != -1:
                res = min(res, abs(j - k))

    return res


# two-pointers, TC:O(NM), M is len(word1), SC:O(1)
def shortestWordDistance2(wordsDict: List[str], word1: str, word2: str) -> int:
    n = len(wordsDict)
    same = word1 == word2
    res = n

    j, k = -1, -1
    for i in range(n):
        word = wordsDict[i]
        if word == word1:
            if same and j != -1:
                res = min(res, i-j)
            j = i
        elif word == word2:
            k = i
        if j != -1 and k != -1:
            res = min(res, abs(j - k))

    return res