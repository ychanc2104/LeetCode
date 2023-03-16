# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/description/


# first thought, bfs, TC:O(N), SC:O(N)
def isCompleteTree(root: Optional[TreeNode]) -> bool:
    stop = False
    queue = [root]
    while queue:
        leafs = []
        for node in queue:
            for child in [node.left, node.right]:
                if not child:
                    stop = True
                    continue
                if stop:
                    return False
                leafs.append(child)
        queue = leafs
    return True


# concise bfs, TC:O(N), SC:O(N)
def isCompleteTree2(root: Optional[TreeNode]) -> bool:
    queue = [root]
    i = 0
    while queue[i]: # encounter null => stop
        queue.append(queue[i].left)
        queue.append(queue[i].right)
        i += 1
    return not any(queue[i:]) # all should be null