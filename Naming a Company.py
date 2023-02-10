# https://leetcode.com/problems/naming-a-company/


import collections

# group by first char, TC:O(NM) M is len of idea and N is len of ideas, SC:O(NM)
def distinctNames(ideas: List[str]) -> int:
    groups = collections.defaultdict(set)
    for idea in ideas:  # TC:O(NM), M is len of idea and N is len of ideas
        groups[idea[0]].add(idea[1:])
    res = 0
    chars = list(groups.keys())
    for i in range(len(chars)):  # TC:O(26*26)
        for j in range(i + 1, len(chars)):
            c1, c2 = chars[i], chars[j]
            n1, n2 = len(groups[c1]), len(groups[c2])
            # if suffix is the same => can't form valid name
            mutual = len(groups[c1] & groups[c2])
            res += (n1 - mutual) * (n2 - mutual) * 2  # *2 is order can be changed
    return res