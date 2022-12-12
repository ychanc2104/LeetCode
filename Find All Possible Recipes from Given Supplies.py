# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/

import collections

# first thought, topsort, TC:O(N+M+Nk), SC:O(Nk)
def findAllRecipes(recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
    # len(recipes): N
    # len(supplies): M
    # avg ingredients: k
    graph = collections.defaultdict(list)
    indegrees = {recipe: len(ingredients[i]) for i, recipe in enumerate(recipes)}  # TC:O(N), SC:O(N)
    for i, ingredient in enumerate(ingredients):  # TC:O(Nk), SC:O(Nk)
        for e in ingredient:
            graph[e].append(recipes[i])
    res = []
    i = 0
    # explore all ingredients
    while i < len(supplies):  # TC:O(M+N+Nk)
        supply = supplies[i]
        for rec in graph[supply]:
            indegrees[rec] -= 1
            if indegrees[rec] == 0:
                res.append(rec)  # bread
                supplies.append(rec)
        i += 1
    return res