# https://leetcode.com/problems/subdomain-visit-count/description/

import collections


# hash, TC:O(N), SC:O(N)
def subdomainVisits(cpdomains: List[str]) -> List[str]:
    memo = collections.defaultdict(int)
    for domain in cpdomains:
        count, url = domain.split(' ')
        url_list = url.split('.')
        for i in range(len(url_list)):
            memo['.'.join(url_list[i:])] += int(count)
    res = []
    for k, v in memo.items():
        res.append(f"{v} {k}")
    return res