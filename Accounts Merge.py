# https://leetcode.com/problems/accounts-merge/
# https://leetcode.com/problems/accounts-merge/discuss/1084738/Python-The-clean-Union-Find-solution-you-are-looking-for

import collections

# dfs, worst case, only one person, N is len(accounts),M is len(accounts[i])
# TC: O(NMlogNM) for the sorting, SC: O(NM) for the graph
def accountsMerge(accounts):
    # build graph, key: email, value: list of account index
    graph = collections.defaultdict(list)
    for i, account in enumerate(accounts):
        for email in account[1:]:
            graph[email].append(i)

    # collect all emails from the same person
    def dfs(i, emails):
        if i not in visit:
            visit.add(i)
            account = accounts[i]
            for email in account[1:]:
                emails.add(email)
                for index in graph[email]:
                    dfs(index, emails)

    # build res
    res = []
    visit = set()
    for i, account in enumerate(accounts):
        if i not in visit:
            # collect all emails
            emails = set()
            dfs(i, emails)
            res.append([account[0]] + sorted(emails))
    return res
# union find
def accountsMerge2(accounts):
    n = len(accounts)
    parent = list(range(n))
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    def union(x, y):
        px, py = find(x), find(y)
        parent[px] = py
    # build graph
    graph = collections.defaultdict(list)
    for i, account in enumerate(accounts):
        for email in account[1:]:
            graph[email].append(i)
    # union
    for i_list in graph.values():
        for i in i_list[1:]:
            union(i_list[0], i)
    # merge account
    merge = {}
    for i in range(n):
        # get parent node
        p = find(i)
        if p not in merge:
            merge[p] = set(accounts[i][1:])
        else:
            merge[p].update(accounts[i][1:])
    res = [[accounts[i][0]] + sorted(list(emails)) for i, emails in merge.items()]
    return res

# union find
def accountsMerge3(accounts):
    n = len(accounts)
    parent = list(range(n))
    # make all child point to its parent
    def find(x):
        if parent[x] != x:
            # find its parent until x==parent[x] (no parent)
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        # y as parent
        parent[px] = py

    email_to_id = collections.defaultdict(list)
    for i, account in enumerate(accounts):
        for email in account[1:]:
            email_to_id[email].append(i)

    for ids in email_to_id.values():
        for id in ids[1:]:
            union(ids[0], id)

    merged_accounts = collections.defaultdict(set)
    for i, account in enumerate(accounts):
        merged_accounts[find(i)].update(account[1:])

    return [[accounts[i][0]] + sorted(emails) for i, emails in merged_accounts.items()]


# union find
class UF:
    def __init__(self, N):
        self.parents = list(range(N))

    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:
    # 196 ms, 82.09%.
    def accountsMerge(self, accounts):
        uf = UF(len(accounts))

        # Creat unions between indexes
        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    uf.union(i, ownership[email])
                ownership[email] = i

        # Append emails to correct index
        ans = collections.defaultdict(list)
        for email, owner in ownership.items():
            ans[uf.find(owner)].append(email)

        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]

# union find, TC:O(NM*alpha) N is len of account and M is len of emails, SC:O(NM)
def accountsMerge4(accounts):

    def find(x):
        px = parent[x]
        if x != px:
            parent[x] = find(px)
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        parent[px] = py
    # TC:O(N), SC:O(N)
    parent = [i for i in range(len(accounts))]
    # SC:O(NM)
    graph = collections.defaultdict(list)
    # TC:O(N)
    for i, account in enumerate(accounts):
        email = account[1:]
        for e in email:
            graph[e].append(i)
    # union accounts, TC:O(NM*alpha), M is average length of emails
    for indices in graph.values():
        # union indices
        for i in range(len(indices) - 1):
            union(indices[i], indices[i + 1])
    # find all,
    for i in range(len(accounts)):
        find(i)
    # print(parent)
    # merge accounts
    res = collections.defaultdict(set)
    for i, px in enumerate(parent):
        res[px].update(accounts[i][1:])
    # print(res)
    return [[accounts[k][0]] + list(sorted(v)) for k, v in res.items()]

# dfs
def accountsMerge5(accounts):
    n = len(accounts)
    graph = collections.defaultdict(set)

    for i in range(n):
        emails = accounts[i][1:]
        for j in range(len(emails)):
            graph[emails[0]].add(emails[j])
            graph[emails[j]].add(emails[0])

    visited = set()
    comp = collections.defaultdict(list)

    def dfs(i, node):
        if node in visited:
            return
        comp[i].append(node)
        visited.add(node)
        for nei in graph[node]:
            if nei in visited:
                continue
            dfs(i, nei)
    # TC:O(NK)
    for i in range(n):
        for email in accounts[i][1:]:
            dfs(i, email)

    # sorting worst case all emails belong to one person, TC:O(NKlogNK)
    res = []
    for i, emails in comp.items():
        res.append([accounts[i][0]] + sorted(emails))
    return res




accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]


