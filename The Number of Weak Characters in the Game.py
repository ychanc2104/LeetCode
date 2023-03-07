# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/


# sort, TC:O(NlogN), SC:O(N)
def numberOfWeakCharacters(properties: List[List[int]]) -> int:
    properties.sort(key=lambda x: (-x[0], x[1]))
    maxDefense = 0
    res = 0
    for a, d in properties:
        if d >= maxDefense:
            maxDefense = d
        else:
            res += 1
    return res

# bucket sort, TC:O(N+M), M is max attack, SC:O(M)
def numberOfWeakCharacters2(properties: List[List[int]]) -> int:
    bucket = [0] * (max(a for a,d in properties) + 2)
    for a, d in properties:
        bucket[a] = max(bucket[a], d)
    for i in range(len(bucket)-2,-1,-1):
        bucket[i] = max(bucket[i], bucket[i+1])
    res = 0
    for a, d in properties:
        if bucket[a+1] > d: # there is bigger defense at a+1 (bigger attack)
            res += 1
    return res