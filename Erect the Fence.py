# https://leetcode.com/problems/erect-the-fence/description/
# https://leetcode.com/problems/erect-the-fence/solutions/1442266/a-detailed-explanation-with-diagrams-graham-scan/

# Graham's Scan Algorithm, TC:O(NlogN) for sorting, SC:O(N)
def outerTrees(trees: List[List[int]]) -> List[List[int]]:
    def check(p1, p2, p3):  # sorted
        dx1 = (p2[0] - p1[0])
        dy1 = (p2[1] - p1[1])
        dx2 = (p3[0] - p1[0])
        dy2 = (p3[1] - p1[1])
        return dy2 * dx1 - dy1 * dx2  # same dir, dy2/dx2 > dy1/dx1

    trees.sort()
    bottom = []  # counterclockwise
    top = []  # clockwise
    for tree in trees:
        while len(bottom) >= 2 and check(bottom[-2], bottom[-1], tree) < 0:
            bottom.pop()
        while len(top) >= 2 and check(top[-2], top[-1], tree) > 0:
            top.pop()
        bottom.append(tuple(tree))
        top.append(tuple(tree))
    return set(bottom + top)