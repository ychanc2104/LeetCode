# https://leetcode.com/problems/course-schedule/

import collections

## dfs, recursive method, TC: O(V+E), vertex and edges, SC:O(V+E)
def canFinish(numCourses: int, prerequisites) -> bool:
    course_pre = {i: [] for i in range(numCourses)}
    for course, pre in prerequisites:
        course_pre[course].append(pre)
    # if visit course twice => cyclic graph
    visited = set()

    def dfs(course):
        if course in visited:
            return False
        if course_pre[course] == []:
            return True
        visited.add(course)
        # print(visited)
        for pre in course_pre[course]:
            if not dfs(pre):
                return False
        ## remove course and backtrack
        visited.remove(course)
        ## mark finish to reduce time complexity
        course_pre[course] = []
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True

## dfs, recursive method, TC: O(V+E), vertex and edges, SC:O(V+E)
def canFinish2(numCourses: int, prerequisites) -> bool:
    memo = collections.defaultdict(list)
    for x in prerequisites:
        memo[x[0]].append(x[1])
    # print(memo)
    visit = set()
    # 1 => 0
    #   <=
    def dfs(course):
        # print(course, visit)
        if course in visit:
            return False
        if course not in memo:
            return True
        pre_list = memo[course]
        visit.add(course)
        for c in pre_list:
            if not dfs(c):
                return False
        visit.remove(course)
        ## mark finished, very important to reduce time complexity
        del memo[course]
        return True
    for i in range(numCourses):
        if not dfs(i):
            return False
    return True

# topsort, Kahn's algorithm
def canFinish3(n, edges):
    """
    :type n: int
    :type edges: List[List[int]]
    :rtype: bool
    """
    # construct graph
    # value is prerequisites set
    graph = {i: set() for i in range(n)}
    # value is count of indegree number
    in_degrees = {i: 0 for i in range(n)}

    for edge in edges:
        graph[edge[0]].add(edge[1])
        in_degrees[edge[1]] += 1

    # init var
    q = collections.deque()
    visited = set()

    # find nodes whose in degree == 0
    for index, in_degree in in_degrees.items():
        if in_degree == 0:
            q.append(index)

    # loop all nodes whose in degree == 0
    while q:
        index = q.popleft()
        visited.add(index)
        for g in graph[index]:
            in_degrees[g] -= 1
            if in_degrees[g] == 0:
                q.append(g)
    return len(visited) == n



# topsort, Kahn's algorithm, TC:O(V+E), SC:O(V+E)
def canFinish4(numCourses: int, prerequisites):
    # build graph and in_degree
    graph = collections.defaultdict(set)
    in_degree = collections.defaultdict(int)
    for course, pre in prerequisites:
        graph[course].add(pre)
        in_degree[pre] += 1
    # find in_degree=0 and add to queue
    queue = collections.deque()
    for i in range(numCourses):
        if in_degree[i] == 0:
            queue.append(i)
    # start from q
    visit = set()
    while queue:
        c = queue.popleft()
        visit.add(c)
        for pre in graph[c]:
            in_degree[pre] -= 1
            # no dependency
            if in_degree[pre] == 0:
                queue.append(pre)
    return len(visit) == numCourses

# topsort, Kahn's algorithm, TC:O(V+E), SC:O(V+E)
def canFinish5(numCourses: int, prerequisites):
    # if cycle detected => return False
    graph = collections.defaultdict(list)
    indegrees = collections.defaultdict(int)
    for cur, pre in prerequisites:
        graph[pre].append(cur)
        indegrees[cur] += 1
        indegrees[pre] += 0

    queue = [c for c, v in indegrees.items() if v == 0]
    n = len(indegrees)  # total courses
    while queue:
        n -= len(queue)
        leafs = []
        for node in queue:
            for nei in graph[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    leafs.append(nei)
        queue = leafs
    return False if n else True


numCourses = 7
prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]

res = canFinish(numCourses, prerequisites)

res2 = canFinish2(numCourses, prerequisites)


n = 7
edges = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]

