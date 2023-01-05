# https://leetcode.com/problems/detect-squares/description/
# https://leetcode.com/problems/detect-squares/solutions/1471958/c-java-python-2-approaches-using-hashmap-with-picture-clean-concise/

class DetectSquares:
    # SC:O(N)
    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = self.points.get(tuple(point), 0) + 1
    # TC:O(N)
    def count(self, point: List[int]) -> int:
        def valid(target): # TC:O(1)
            count = 1
            for point in target:
                if point not in self.points:
                    return 0
                count *= self.points[point]
            return count
        res = 0
        for x, y in self.points.keys():
            if x == point[0] and y != point[1]: # find left and right
                count = self.points[(x,y)]
                dist = abs(y - point[1])
                target_left = ((x-dist, y), (x-dist, point[1]))
                target_right = ((x+dist, y), (x+dist, point[1]))
                res += count*valid(target_left) + count*valid(target_right)
        return res


# only find its diagonal points
class DetectSquares2:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] = self.points.get(tuple(point), 0) + 1

    # TC:O(N)
    def count(self, point: List[int]) -> int:
        res = 0
        for (x, y), count in self.points.items():
            if x == point[0] or y == point[1] or abs(x-point[0]) != abs(y-point[1]): # find diagonal points and square
                continue
            res += count * self.points.get((x, point[1]), 0) * self.points.get((point[0], y), 0)
        return res

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)