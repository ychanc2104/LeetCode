# https://leetcode.com/problems/best-team-with-no-conflicts/description/
# https://leetcode.com/problems/best-team-with-no-conflicts/solutions/899475/fairly-easy-dp/


# top down dp, TC:O(N^2), SC:O(N^2)
def bestTeamScore(scores: List[int], ages: List[int]) -> int:
    people = sorted([(age, score) for age, score in zip(ages, scores)])

    @functools.lru_cache(None)
    def helper(i, prev=-1):
        if i == len(scores):
            return 0
        # compare skip and choose
        choose = 0
        if prev == -1 or people[i][0] == people[prev][0] or people[i][1] >= people[prev][1]:
            choose = people[i][1] + helper(i + 1, i)
        skip = helper(i + 1, prev)
        return max(skip, choose)

    # 1,1,2,2
    # 5,5,6,4

    return helper(0)


# bottom-up dp, TC:O(N^2), SC:O(N)
def bestTeamScore(scores: List[int], ages: List[int]) -> int:
    people = sorted([(age,score) for age,score in zip(ages,scores)])
    n = len(scores)
    dp = [0] * n # dp[i]: max score end with i
    for i in range(n):
        for j in range(i,-1,-1): # prev
            if people[i][1]>=people[j][1]:
                dp[i] = max(dp[i], dp[j] + people[i][1])
    return max(dp)

