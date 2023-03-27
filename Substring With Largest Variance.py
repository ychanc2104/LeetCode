# https://leetcode.com/problems/substring-with-largest-variance/
# https://leetcode.com/problems/substring-with-largest-variance/solutions/2041108/python3-enumerate-all-a-b-combinations-and-do-maximum-subarray/

import collections, itertools


# use combinations, TC:O(N^3), SC:O(N)
def largestVariance(s: str) -> int:
    res = 0
    # chars = list(set(s))  # combination 2
    counter = collections.Counter(s)

    def comb(arr, k):
        n = len(arr)
        res_comb = []
        path = []

        def backtrack(i):
            if len(path) == k:
                res_comb.append(path[:])
                return
            for j in range(i, n):
                path.append(arr[j])
                backtrack(j + 1)
                path.pop()

        backtrack(0)
        return res_comb

    for a, b in comb(list(counter.keys()), 2):
        for _ in range(2):
            a, b = b, a
            flag1, flag2 = False, False
            temp = 0
            remain_b = counter[b]
            for c in s:
                if c != a and c != b: continue
                if c == a:
                    temp += 1
                    flag1 = True
                elif c == b:
                    if temp > 0 or remain_b == 1:
                        temp -= 1
                        flag2 = True
                    remain_b -= 1
                # temp = max(temp, tempMax+tempMin)
                if flag1 and flag2:
                    res = max(res, temp)
    return res

# use permutations, TC:O(N^3), SC:O(N)
def largestVariance2(s: str) -> int:
    res = 0
    counter = collections.Counter(s)
    for a,b in itertools.permutations(counter, 2):
        flag1, flag2 = False, False
        temp = 0
        remain_b = counter[b]
        for c in s:
            if c!=a and c!=b: continue
            if c == a:
                temp += 1
                flag1 = True
            elif c == b:
                if temp > 0 or remain_b==1:
                    temp -= 1
                    flag2 = True
                remain_b -= 1
            # temp = max(temp, tempMax+tempMin)
            if flag1 and flag2:
                res = max(res, temp)
    return res

# use two loops, TC:O(N^3), SC:O(N)
def largestVariance3(s: str) -> int:
    res = 0
    counter = collections.Counter(s)
    chars = list(counter.keys()) # combination 2
    for i in range(len(chars)):
        for j in range(len(chars)):
            if i == j: continue
            a, b = chars[i], chars[j]
            flag1, flag2 = False, False
            temp = 0
            remain_b = counter[b]
            for c in s:
                if c != a and c != b: continue
                if c == a:
                    temp += 1
                    flag1 = True
                elif c == b:
                    if temp > 0 or remain_b==1:
                        temp -= 1
                        flag2 = True
                    remain_b -= 1
                if flag1 and flag2:
                    res = max(res, temp)
    return res
