# https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/1597523/Python-Heapq-Priority-queue
# https://leetcode.com/problems/maximum-profit-in-job-scheduling/discuss/918804/Python-Top-Down-and-Bottom-Up-DP-7-lines-each

import heapq

# first thought, dfs (TLE)
def jobScheduling(startTime, endTime, profit) -> int:
    def dfs(i, pathSum=0):
        res[0] = max(res[0], pathSum)
        visit.add(i)
        # find next job
        for j in range(i + 1, len(startTime)):
            if pairs[j][0] >= pairs[i][1]:
                dfs(j, pathSum + pairs[j][2])

    n = len(startTime)
    res = [0]
    pairs = [(s, e, p) for s, e, p in sorted(zip(startTime, endTime, profit))]
    visit = set()
    for i in range(n):
        if i in visit:
            continue
        dfs(i, pairs[i][2])
    return res[0]


# bfs(TLE)
def jobScheduling2(startTime, endTime, profit) -> int:
    n = len(startTime)
    res = 0
    pairs = [(s,e,-p) for s,e,p in sorted(zip(startTime, endTime, profit))]
    heap = [(pairs[i][2], i) for i in range(n)] # (sum, index)
    while heap:
        pathSum, i = heapq.heappop(heap)
        res = max(res, -pathSum)
        for j in range(i+1, n):
            if pairs[j][0] >= pairs[i][1]:
                heapq.heappush(heap, (pathSum + pairs[j][2], j))
    return res


# priority queue, TC:O(NlogN), SC:O(N)
def jobScheduling3(startTime, endTime, profit) -> int:
    n = len(startTime)
    # TC:O(nlogn)
    pairs = sorted(zip(startTime, endTime, profit))
    heap = []
    maxSum = 0
    # TC:O(nlogn)
    for i in range(n):
        # start from i
        start = pairs[i][0]
        # get max pathSum containing i
        while heap and start >= heap[0][0]: # current start >= previous end
            prev_end, pathSum = heapq.heappop(heap) # previous
            maxSum = max(maxSum, pathSum)
        heapq.heappush(heap, (pairs[i][1], maxSum + pairs[i][2]))
    # TC:O(n)
    for e, pathSum in heap:
        maxSum = max(maxSum, pathSum)
    return maxSum

startTime = [6,15,7,11,1,3,16,2]
endTime = [19,18,19,16,10,8,19,8]
profit = [2,9,1,19,5,7,3,19]


startTime = [341,22,175,424,574,687,952,439,51,562,962,890,250,47,945,914,835,937,419,343,125,809,807,959,403,861,296,39,802,562,811,991,209,375,78,685,592,409,369,478,417,162,938,298,618,745,888,463,213,351,406,840,779,299,90,846,58,235,725,676,239,256,996,362,819,622,449,880,951,314,425,127,299,326,576,743,740,604,151,391,925,605,770,253,670,507,306,294,519,184,848,586,593,909,163,129,685,481,258,764]
endTime = [462,101,820,999,900,692,991,512,655,578,996,979,425,893,975,960,930,991,987,524,208,901,841,961,878,882,412,795,937,807,957,994,963,716,608,774,681,637,635,660,750,632,948,771,943,801,985,476,532,535,929,943,837,565,375,854,174,698,820,710,566,464,997,551,884,844,830,916,970,965,585,631,785,632,892,954,803,764,283,477,970,616,794,911,771,797,776,686,895,721,917,920,975,984,996,471,770,656,977,922]
profit = [85,95,14,72,17,3,86,65,50,50,42,75,40,87,35,78,47,74,92,10,100,29,55,57,51,34,10,96,14,71,63,99,8,37,16,71,10,71,83,88,68,79,27,87,3,58,56,43,89,31,16,9,49,84,62,30,35,7,27,34,24,33,100,25,90,79,58,21,31,30,61,46,36,45,85,62,91,54,28,63,50,69,48,36,77,39,19,97,20,39,48,72,37,67,72,46,54,37,53,30]


res = jobScheduling(startTime, endTime, profit)
res2 = jobScheduling2(startTime, endTime, profit)

