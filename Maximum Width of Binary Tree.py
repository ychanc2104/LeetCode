# https://leetcode.com/problems/maximum-width-of-binary-tree/


import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# level-order BFS, TC:O(N), SC:O(N)
def widthOfBinaryTree(root) -> int:
    count = 1
    queue = [(root, 1)]
    while queue:
        leafs = []
        for node, level in queue:
            if node.left:
                leafs.append((node.left, 2 * level))
            if node.right:
                leafs.append((node.right, 2 * level + 1))
        if leafs:
            count = max(count, leafs[-1][1] - leafs[0][1] + 1)
        queue = leafs
    return count

# level-order BFS, TC:O(N), SC:O(W)
def widthOfBinaryTree2(root) -> int:
    # root:0, 2i+1 and 2i+2

    queue = collections.deque([(root, 0, 0)])
    index_arr = []
    while queue:
        node, level, index = queue.popleft()
        if len(index_arr) <= level:
            index_arr.append([index])
        else:
            index_arr[level].append(index)
        if node.left:
            queue.append((node.left, level + 1, index * 2 + 1))
        if node.right:
            queue.append((node.right, level + 1, index * 2 + 2))
    # print(res)
    # width_arr = [max(arr) - min(arr) + 1 for arr in index_arr]
    return max(max(arr) - min(arr) + 1 for arr in index_arr)

# level-order BFS, TC:O(N), SC:O(W)
def widthOfBinaryTree3(root) -> int:
    # root:0, 2i+1 and 2i+2
    queue = [(root, 0)]
    res = 1
    while queue:
        leaves = []
        for i in range(len(queue)):
            node, index = queue[i]
            if node.left:
                leaves.append((node.left, 2*index+1))
            if node.right:
                leaves.append((node.right, 2*index+2))
        if not leaves: break
        res = max(res, leaves[-1][1] - leaves[0][1] + 1)
        queue = leaves
    return res


# dfs, TC:O(N), SC:O(W)
def widthOfBinaryTree4(root: Optional[TreeNode]) -> int:
    # root:0, 2i+1 and 2i+2
    index_table = collections.defaultdict(list)

    def dfs(node, level=0, i=0):
        if not node: return
        dfs(node.left, level + 1, 2 * i + 1)
        dfs(node.right, level + 1, 2 * i + 2)
        index_table[level].append(i)

    dfs(root)
    # print(index_table)
    return max(max(w) - min(w) + 1 for w in index_table.values())

# dfs, TC:O(N), SC:O(W)
def widthOfBinaryTree5(root: Optional[TreeNode]) -> int:
    memo = []
    def helper(root, depth, i):
        if not root:
            return 0
        if len(memo) < depth+1:
            memo.append(i)
        memo[depth] = min(memo[depth], i)
        left = helper(root.left, depth+1, 2*i+1)
        right = helper(root.right, depth+1, 2*i+2)
        return max(i - memo[depth] + 1, left, right)

    return helper(root, 0, 0)