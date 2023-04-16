# https://leetcode.com/problems/boats-to-save-people/description/


# greedy, TC:O(NlogN), SC:O(N) for sorting
def numRescueBoats(people: List[int], limit: int) -> int:
    L, R = 0, len(people) - 1
    people.sort()
    res = 0
    while L <= R:  # two people at most
        if people[L] + people[R] <= limit:
            L += 1
        R -= 1
        res += 1
    return res
