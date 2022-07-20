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
    n = len(temperatures)
    hottest = 0
    answer = [0] * n
    # bottom-up
    for curr_day in range(n - 1, -1, -1):
        current_temp = temperatures[curr_day]
        if current_temp >= hottest:
            hottest = current_temp
            # no possibility to get warmer, use 0(default)
            continue

        days = 1
        while temperatures[curr_day + days] <= current_temp:
            # Use information from answer to search for the next warmer day
            # directly jump to the pos is greater than temperatures[curr_day + days]
            days += answer[curr_day + days]
        answer[curr_day] = days

    return answer