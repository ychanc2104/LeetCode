# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/solutions/37484/7-lines-iterative-real-o-1-space/


import collections

# first thought, dfs, TC:O(N), SC:O(N)
def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    memo = collections.defaultdict(list)

    def helper(root, h=0):
        if not root: return
        if memo[h]:
            root.next = memo[h][-1]
        else:
            root.next = None
        memo[h].append(root)
        helper(root.right, h + 1)
        helper(root.left, h + 1)

    helper(root)
    return root


# bfs, TC:O(N), SC:O(N)
def connect2(root: 'Optional[Node]') -> 'Optional[Node]':

    queue = [root]
    while queue and root:
        leafs = []
        lastNode = None
        for node in queue:
            node.next = lastNode
            for nei in [node.right, node.left]:
                if not nei: continue
                leafs.append(nei)
            lastNode = node
        queue = leafs
    return root



# best, TC:O(N), SC:O(1)
def connect3(root: 'Optional[Node]') -> 'Optional[Node]':
    leftmost = root
    while leftmost and leftmost.left:
        node = leftmost
        # connect all its child
        while node:
            node.left.next = node.right
            # from its parents's next.left
            node.right.next = node.next.left if node.next else None
            node = node.next
        # move to next level
        leftmost = leftmost.left
    return root