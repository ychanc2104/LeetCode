# https://leetcode.com/problems/course-schedule/



## dfs, recursive method, TC: O(V+E), vertex and edges
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

numCourses = 7
prerequisites = [[1,0],[0,3],[0,2],[3,2],[2,5],[4,5],[5,6],[2,4]]

res = canFinish(numCourses, prerequisites)

