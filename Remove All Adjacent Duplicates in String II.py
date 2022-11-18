# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/


# first thought, two stack, TC:O(N), SC:O(N)
def removeDuplicates(s: str, k: int) -> str:
    stack = []
    count_stack = []
    for l in s:
        if stack and stack[-1] == l and count_stack[-1] == (k - 1):  # to remove
            while stack and stack[-1] == l:
                stack.pop()
            count_stack.pop()
        else:
            if stack and stack[-1] == l:
                count_stack[-1] += 1
            else:
                count_stack.append(1)
            stack.append(l)

    return ''.join(stack)

# one stack to store letter and frequency, TC:O(N), SC:O(N)
def removeDuplicates2(s: str, k: int) -> str:
    stack = [] # store (letter,freq)
    for l in s:
        if stack and stack[-1][0] == l:
            stack[-1][1] += 1
            if stack[-1][1] == k: # to remove
                stack.pop()
        else:
            stack.append([l, 1])
    return ''.join([s*f for s,f in stack])