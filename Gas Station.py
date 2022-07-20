# https://leetcode.com/problems/gas-station/


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


# def canCompleteCircuit2(gas, cost) -> int:



gas = [1,2,3,4,3]
cost = [3,4,5,1,2]

res = canCompleteCircuit(gas, cost)