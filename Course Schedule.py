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


numCourses = 7
prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]

res = canFinish(numCourses, prerequisites)

res2 = canFinish2(numCourses, prerequisites)
