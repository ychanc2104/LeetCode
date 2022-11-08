# https://leetcode.com/problems/make-the-string-great/description/


# first thought, stack, TC:O(N), SC:O(N)
def makeGood(s: str) -> str:
    def check(l1, l2):
        return abs(ord(l1) - ord(l2)) == ord('a') - ord('A') # 32

    stack = []
    for i in range(len(s)):
        if stack and check(stack[-1], s[i]):
            stack.pop()
        else:
            stack.append(s[i])
    return ''.join(stack)
