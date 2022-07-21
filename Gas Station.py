# https://leetcode.com/problems/gas-station/
# https://leetcode.com/problems/gas-station/discuss/860347/Python-simple-and-very-short-explained-solution-O(n)-O(1)-faster-than-98

# first thought, TC:O(n^2),
def canCompleteCircuit(gas, cost) -> int:
    # unique ans, return gas station index which can finish traversing
    # if not, return -1
    for i in range(len(gas)):
        j = 1
        current_gas = gas[i] - cost[i]
        while current_gas>=0 and j < len(gas):
            index = i+j
            index -= len(gas) if index>=len(gas) else 0
            print(f"station: {i}, index: {index} ,gas: {current_gas}", j)
            current_gas += gas[index] - cost[index]
            print(f"station: {i}, index: {index} ,gas: {current_gas}", j)
            j += 1
        if current_gas>=0:
            return i
    return -1

# TC:O(N), SC:O(1)
def canCompleteCircuit2(gas, cost) -> int:
    # unique ans, return gas station index which can finish traversing
    # if not, return -1
    substract = [gas[i] - cost[i] for i in range(len(gas))]
    if sum(substract) < 0:
        return -1

    curr_sum = 0
    res = 0
    for i in range(len(gas)):
        curr_sum += gas[i] - cost[i]
        if curr_sum < 0:
            curr_sum = 0
            res = i + 1
    return res


gas = [1,2,3,4,3]
cost = [3,4,5,1,2]

res = canCompleteCircuit(gas, cost)