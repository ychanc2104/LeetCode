# https://leetcode.com/problems/process-tasks-using-servers/


# two heaps, TC:O(N+MlogN), SC:O(N)
def assignTasks(servers: List[int], tasks: List[int]) -> List[int]:
    waitting = [[w, idx, 0] for idx, w in enumerate(servers)]  # idle (weight,idx,time), TC:O(N)
    heapq.heapify(heap1) # TC:O(N)
    running = []  # running, (time,weight,idx)
    res = []
    for clock, t in enumerate(tasks): # TC:O(M)
        # check, running => waitting
        while (running and running[0][0] <= clock) or not waitting:
            idle = heapq.heappop(running)  # pop first to waitting if waitting is ran out
            heapq.heappush(waitting, [idle[1], idle[2], idle[0]])  # running to idle
        weight, idx, time = heapq.heappop(waitting) # TC:O(logN)
        heapq.heappush(running, [max(clock, time) + t, weight, idx])  # choose normal colck or jumped clock
        res.append(idx)
    return res