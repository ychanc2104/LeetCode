# https://leetcode.com/problems/fraction-to-recurring-decimal/description/
# https://leetcode.com/problems/fraction-to-recurring-decimal/solutions/180004/python-4-lines-32ms-beats-100-with-explanation/?orderBy=most_votes


# first thought, recursive, TC:O(), SC:O()
def fractionToDecimal(numerator: int, denominator: int) -> str:
    memo = {}
    path = []

    def helper(n, d, fold):
        if n % d == 0:
            path.append(str(n // d))
        elif n in memo and memo[n]:  # don't insert at index 0
            path.insert(memo[n], '(')
            path.append(')')
        elif n < d:
            if '.' not in memo:
                if not path:
                    path.append('0')
                memo['.'] = len(path)
                path.append('.')
            else:
                memo[n] = len(path)
                path.append('0')
            helper(n * 10, d, fold * 10)
        elif n > d:
            memo[n] = len(path)
            path.append(str(n // d))
            if '.' not in memo:
                memo['.'] = len(path)
                path.append('.')
            helper((n % d) * 10, d, 10)

    if numerator == 0:
        return '0'
    if numerator * denominator < 0:
        path.append('-')
    helper(abs(numerator), abs(denominator), 1)
    return ''.join(path)

# clean, recursive, TC:O(), SC:O()
def fractionToDecimal2(numerator: int, denominator: int) -> str:
    memo = {}
    path = []

    def helper(n, d):
        if n % d == 0:
            path.append(str(n // d))
            return
        if n in memo:  # repeating
            path[memo[n]:] = ['('] + path[memo[n]:] + [')']
            return
        memo[n] = len(path)
        path.append(str(n // d))
        helper((n % d) * 10, d)

    if numerator == 0:
        return '0'
    if numerator * denominator < 0:
        path.append('-')
    numerator, denominator = abs(numerator), abs(denominator)
    path.append(str(numerator // denominator))
    
    if numerator % denominator:
        path.append('.')
        helper((numerator % denominator) * 10, denominator)
    return ''.join(path)