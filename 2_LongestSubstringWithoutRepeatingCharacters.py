class Solution:
    def __init__(self, s):
        self.ans = self.lengthOfLongestSubstring(s)

    def lengthOfLongestSubstring(self, s):
        dt = ""
        L = 0
        for string in s:
            if string not in dt:
                dt += string
            elif L <= len(dt):  ## repeat but refresh L
                L = len(dt)
                i2 = dt.find(string)+1
                dt = dt[i2:] + string
            else: ## repeat but len(dt) < L, no need to refresh
                i2 = dt.find(string)+1
                dt = dt[i2:] + string
        return max(L, len(dt))


s = "abcabcbb"
A = Solution(s)