# https://leetcode.com/problems/copy-list-with-random-pointer/
# https://leetcode.com/problems/copy-list-with-random-pointer/solutions/43491/a-solution-with-constant-space-complexity-o-1-and-linear-time-complexity-o-n/

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

# first thought, use hash table and dfs, TC:O(N), SC:O(N)
def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    memo = {}

    def dfs(node):
        if not node:
            return None
        if node in memo:
            return memo[node]
        new_node = Node(node.val)
        memo[node] = new_node
        new_node.next = dfs(node.next)
        new_node.random = dfs(node.random)
        return new_node

    return dfs(head)

# without memo, TC:O(N), SC:O(1) no extra space except clone
def copyRandomList2(head: 'Optional[Node]') -> 'Optional[Node]':
    if not head: return None
    # build weaved LL
    weaved = dummy = head
    while weaved:
        weaved.next = Node(weaved.val, next=weaved.next)
        weaved = weaved.next.next
    # assign random to correct pos
    weaved = dummy # locate at original LL
    while weaved:
        weaved.next.random = weaved.random.next if weaved.random else None # use cloned node
        weaved = weaved.next.next
    # separate weaved, A->A'->B->B'->C->C'->None
    res = res_dummy = dummy.next
    while res.next: # res point at cloned node
        res_next = res.next.next
        res.next = res_next
        res = res.next
    return res_dummy