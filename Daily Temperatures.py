# https://leetcode.com/problems/daily-temperatures/


# first thought, TC:O(n^2), time exceeded
def dailyTemperatures(temperatures):
    res = []
    for i in range(len(temperatures) - 1):
        count = 1
        for j in range(i + 1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                res.append(count)
                break
            count += 1
            if j == len(temperatures) - 1:
                res.append(0)
    res.append(0)
    return res


# monotonic stack, TC:O(N), SC:O(N)
def dailyTemperatures2(temperatures):
    res = [0] * len(temperatures)
    stack = []
    for day, temp in enumerate(temperatures):
        while stack and temp > stack[-1][1]:
            day0, temp0 = stack.pop()
            # assign res at that day0 if temp>temp0 (get warmer)
            res[day0] = day - day0
        stack.append((day, temp))
    return res

# monotonic stack, TC:O(N), SC:O(1)
def dailyTemperatures3(temperatures):
    stack = []  # put index
    res = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
        # stack descend until temp > temperatures[stack[-1]]
        while stack and temp > temperatures[stack[-1]]:
            index = stack.pop()
            res[index] = i - index
        else:
            stack.append(i)
    return res