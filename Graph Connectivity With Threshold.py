# https://leetcode.com/problems/graph-connectivity-with-threshold/
# https://leetcode.com/problems/graph-connectivity-with-threshold/solutions/899595/c-java-python-union-find-o-n-logn-q/

# first thought union find, TC:O(N*sqrt(N)), SC:O(N)
def areConnected(n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
    # union n with all its factors which is greater than threshold
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = py

    parents = [i for i in range(n + 1)]
    for i in range(1, n + 1):
        for f in range(1, int(i ** 0.5) + 1):  # to sqrt(i)
            if i % f == 0:
                if f > threshold:
                    union(i, f)
                if i // f > threshold:
                    union(i, i // f)
    return [find(x) == find(y) for x, y in queries]

# union find, TC:O(N*logN), SC:O(N)
def areConnected2(n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
    # union n with all its factors which is greater than threshold
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x, y):
        px, py = find(x), find(y)
        parents[px] = py

    parents = [i for i in range(n + 1)]
    for f in range(threshold + 1, n + 1):
        # TC:O(1+1/2+1/3+...+1/N) ~ O(logN), harmonic series ~ logN + r for n terms
        for i in range(2 * f, n + 1, f):  # increasment f
            # union with all integer with factor f
            union(i, f)

    return [find(x) == find(y) for x, y in queries]