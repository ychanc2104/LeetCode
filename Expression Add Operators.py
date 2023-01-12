# https://leetcode.com/problems/expression-add-operators/


# dfs, TC:O(N*4^N), SC:O(N)
def addOperators(num: str, target: int) -> List[str]:
    # get all opt possibilities, +-*
    res = []

    def dfs(num, formula='', curSum=0, preNum=0):
        if not num and curSum == target:
            res.append(formula)
            return
        for i in range(len(num)):
            val = num[:i + 1]
            if len(val) > 1 and val[0] == '0': continue
            if formula:
                dfs(num[i + 1:], (formula + '+' + val), curSum + int(val), int(val))
                dfs(num[i + 1:], (formula + '-' + val), curSum - int(val), -int(val))
                dfs(num[i + 1:], (formula + '*' + val), preNum * int(val) + (curSum - preNum), preNum * int(val))
            else:
                dfs(num[i + 1:], val, curSum + int(val), int(val))

    dfs(num)
    return res

# dfs + backtracking, TC:O(N*4^N), SC:O(N)
def addOperators2(num: str, target: int) -> List[str]:
    res = []
    formula = []
    def dfs(num, curSum=0, preNum=0):
        if not num and curSum == target:
            res.append(''.join(formula))
            return
        for i in range(len(num)):
            val = num[:i + 1]
            if len(val) > 1 and val[0] == '0': continue
            if formula:
                formula.append('+'); formula.append(val)
                dfs(num[i + 1:], curSum + int(val), int(val))
                formula.pop(); formula.pop()
                formula.append('-'); formula.append(val)
                dfs(num[i + 1:], curSum - int(val), -int(val))
                formula.pop(); formula.pop()
                formula.append('*'); formula.append(val)
                dfs(num[i + 1:], preNum * int(val) + (curSum - preNum), preNum * int(val))
                formula.pop(); formula.pop()
            else:
                formula.append(val)
                dfs(num[i + 1:], curSum + int(val), int(val))
                formula.pop()
    dfs(num)
    return res


# backtracking, TC:O(N*4^N), SC:O(N)
def addOperators3(num: str, target: int) -> List[str]:
    N = len(num)
    answers = []
    def recurse(index, prev_operand, current_operand, value, string):

        # Done processing all the digits in num
        if index == N:

            # If the final value == target expected AND
            # no operand is left unprocessed
            if value == target and current_operand == 0:
                answers.append("".join(string[1:]))
            return

        # Extending the current operand by one digit
        current_operand = current_operand*10 + int(num[index])
        str_op = str(current_operand)

        # To avoid cases where we have 1 + 05 or 1 * 05 since 05 won't be a
        # valid operand. Hence this check
        if current_operand > 0:

            # NO OP recursion
            recurse(index + 1, prev_operand, current_operand, value, string)

        # ADDITION
        string.append('+'); string.append(str_op)
        recurse(index + 1, current_operand, 0, value + current_operand, string)
        string.pop();string.pop()

        # Can subtract or multiply only if there are some previous operands
        if string:

            # SUBTRACTION
            string.append('-'); string.append(str_op)
            recurse(index + 1, -current_operand, 0, value - current_operand, string)
            string.pop();string.pop()

            # MULTIPLICATION
            string.append('*'); string.append(str_op)
            recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
            string.pop();string.pop()
    recurse(0, 0, 0, 0, [])
    return answers