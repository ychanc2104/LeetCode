# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

# first thought, TC:O(N), SC:O(N)
def removeDuplicates(s: str) -> str:
    stack = []
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    return ''.join(stack)