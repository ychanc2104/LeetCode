# https://leetcode.com/problems/dota2-senate/
# https://leetcode.com/problems/dota2-senate/solutions/105858/java-c-very-simple-greedy-solution-with-explanation/


import collections

# two queue, TC:O(N), SC:O(N)
def predictPartyVictory(senate: str) -> str:
    n = len(senate)
    queueR = collections.deque([])
    queueD = collections.deque([])
    for i in range(n):
        if senate[i] == 'R':
            queueR.append(i)
        else:
            queueD.append(i)

    while queueR and queueD:
        ir, id = queueR.popleft(), queueD.popleft()
        if ir < id:
            queueR.append(ir + n)
        else:
            queueD.append(id + n)

    return "Radiant" if queueR else "Dire"