# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/780232/Backtracking-Python-problems%2B-solutions-interview-prep


# dfs, TC: O(N*4^N), SC: O(N)
def letterCombinations(digits: str):
    digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    # permute
    choices = []
    for s in digits:
        if s in digit_map:
            choices.append(digit_map[s])
    res = []
    def dfs(i, path):
        if i >= len(choices):
            if path:
                # O(N)
                res.append(path)
            return
        # 4*4*4*...(N times) => N*4^N, SC:O(N)
        for l in choices[i]:
            # 4 max length, each call N = len(digits) times

            dfs(i + 1, path + l)
    dfs(0, '')
    return res
# backtracking, TC: O(N*4^N), SC: O(N)
def letterCombinations2(digits: str):
    digit_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    # permute
    choices = []
    for s in digits:
        if s in digit_map:
            choices.append(digit_map[s])
    res = []

    def backtrack(i, path):
        if i >= len(choices):
            if path:
                res.append(''.join(path))
            return
        for l in choices[i]:
            path.append(l)
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return res

digits = "23"

res = letterCombinations(digits)


