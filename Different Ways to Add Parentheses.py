# https://leetcode.com/problems/different-ways-to-add-parentheses/
# https://leetcode.com/problems/different-ways-to-add-parentheses/solutions/1294189/easy-solution-faster-than-100-explained-with-diagrams/
# https://leetcode.com/problems/different-ways-to-add-parentheses/solutions/66419/python-easy-to-understand-concise-solution-with-memorization/

# TC:O(C(n)) C is Catalan number, SC:O()
def diffWaysToCompute(expression: str) -> List[int]:
    opt = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
    def helper(exp):
        res = []
        for i in range(len(exp)):
            if exp[i] in '+-*':
                left = helper(exp[:i])
                right = helper(exp[i + 1:])
                for l in left:
                    for r in right:
                        res.append(opt[exp[i]](l, r))
        return res if res else [int(exp)]

    return helper(expression)

# dp + dfs
def diffWaysToCompute2(expression: str) -> List[int]:
    opt = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
    memo = {}

    def helper(exp):
        if exp in memo:
            return memo[exp]
        if exp.isdigit():
            memo[exp] = [int(exp)]
            return memo[exp]
        res = []
        for i in range(len(exp)):
            if exp[i] in '+-*':
                left = helper(exp[:i])
                right = helper(exp[i + 1:])
                for l in left:
                    for r in right:
                        res.append(opt[exp[i]](l, r))
        memo[exp] = res
        return memo[exp]

    return helper(expression)