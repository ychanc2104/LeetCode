# https://leetcode.com/problems/valid-number/description/

"""
Rules

    Digits
        First of all, there must always be at least one digit in the input for it to form a valid number. Let's use a variable seenDigit to indicate whether we have seen a digit yet.

    Signs
        If a sign is present, it must be the first character in a decimal number or integer. In a valid number, there are two possible locations for these signs - at the front of the number, or right after an exponent ("e" or "E") e.g., -63e+7. Therefore, if we see a sign, and it is not the first character of the input, and does not come immediately after an exponent ("e" or "E"), then we know the number is not valid.

    Exponents ("e" or "E")
        There cannot be more than one exponent in a valid number, so we will use a variable seenExponent to indicate whether we have already seen an exponent.
        An exponent must appear after a decimal number or an integer. This means if we see an exponent, we must have already seen a digit.

    Dots
        There cannot be more than one dot in a valid number, since only integers are allowed after an exponent, so there cannot be more than one decimal number. We will use a variable seenDot to indicate whether we have seen a dot.
        If we see a dot appear after an exponent, the number is not valid, because integers cannot have dots.

    Anything else
        Seeing anything else instantly invalidates the input.

"""


# check by rules, TC:O(N), SC:O(1)
def isNumber(s: str) -> bool:
    seen_digit = seen_exponent = seen_dot = False
    for i, c in enumerate(s):
        if c.isdigit():
            seen_digit = True
        elif c in 'eE':  # (X) eE,
            if seen_exponent or not seen_digit:
                return False
            seen_exponent = True
            seen_digit = False  # 5e.93 in . case
        elif c in '-+':  # only in first index or after 'eE'
            if i > 0 and s[i - 1] not in 'eE':  # (X) .-5, 1+2E (O)1E+3
                return False

        elif c == '.':  # (X) 3e.1, 6e6.5,
            if seen_dot or seen_exponent:
                return False
            seen_dot = True
        else:
            return False
    return seen_digit