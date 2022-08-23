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



## dp, SC, O(n), TC: O(1)
def numDecodings4(s: str) -> int:
    # 11111 => 111(f0) + 11 and 1111(f1) + 1
    # 11110 => 111(f0) + 10
    # 11133 => 1113(f1) + 3
    if s[0] == "0": return 0
    f0, f1, f2 = 1, 1, 1
    for i in range(1,len(s)):
        if s[i] == "0":
            if s[i-1:i+1]>"26" or s[i-1]=="0":
                return 0
            f2 = f0
        elif s[i-1:i+1]<"10" or s[i-1:i+1]>"26":
            f2 = f1
        else:
            f2 = f0 + f1
        f0, f1 = f1, f2
    return f2


## dp, SC, O(n), TC: O(1)
def numDecodings5(s: str) -> int:
    # 11111 => 111(f0) + 11 and 1111(f1) + 1
    # 11110 => 111(f0) + 10
    # 11133 => 1113(f1) + 3
    if s[0] == "0": return 0
    f0, f1 = 1, 1
    for i in range(1,len(s)):
        f2 = 0
        if s[i] != "0":
            f2 = f1
        if "10"<=s[i-1:i+1]<="26":
            f2 += f0
        f0, f1 = f1, f2
    return f1

s = "111111"

res = numDecodings(s)

res2 = numDecodings2(s)


a={1:'1', 2:'2'}