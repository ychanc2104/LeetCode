# https://leetcode.com/problems/decode-ways/
# https://leetcode.com/problems/decode-ways/discuss/30379/1-liner-O(1)-space


## Space, O(n), Time: O(n), top down dp
def numDecodings(s: str) -> int:
    dp = {len(s): 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == '0':
            return 0
        res = dfs(i + 1)
        if i + 2 <= len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
            res += dfs(i + 2)
        dp[i] = res
        return res

    # dfs(0)
    # print(dp)

    return dfs(0)

## Space, O(n), Time: O(n), bottom-up dp
def numDecodings2(s: str) -> int:
    dp = {}
    for i in range(len(s), -1, -1):
        print(i)
        if i == len(s):
            dp[i] = 1
        elif s[i]=='0':
            dp[i] = 0
        else:
            dp[i] = dp[i + 1]
            if i + 2 <= len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                dp[i] += dp[i + 2]
    return dp[0]

## Space, O(1), Time: O(n), bottom-up dp
def numDecodings3(s: str) -> int:
    f0, f1 = 0, 1
    for i in range(len(s), -1, -1):
        # print(i)
        if i == len(s):
            f2 = 1
        elif s[i] == '0':
            f2 = 0
        else:
            f2 = f1
            if i + 2 <= len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456')):
                f2 += f0
        f0, f1 = f1, f2
    return f2


s = "111111"

res = numDecodings(s)

res2 = numDecodings2(s)


a={1:'1', 2:'2'}