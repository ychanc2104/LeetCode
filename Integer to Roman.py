# https://leetcode.com/problems/integer-to-roman/description/


# first thought, TC:O(), SC:O()
def intToRoman(num: int) -> str:
    res = []
    while num > 0:
        if num >= 1000:
            count = num // 1000
            res.append(count * 'M')
            num -= count * 1000
        elif num >= 900:
            res.append('CM')
            num -= 900
        elif num >= 500:
            res.append('D')
            num -= 500
        elif num >= 400:
            res.append('CD')
            num -= 400
        elif num >= 100:
            count = num // 100
            res.append(count * 'C')
            num -= count * 100
        elif num >= 90:
            res.append('XC')
            num -= 90
        elif num >= 50:
            res.append('L')
            num -= 50
        elif num >= 40:
            res.append('XL')
            num -= 40
        elif num >= 10:
            count = num // 10
            res.append(count * 'X')
            num -= count * 10
        elif num >= 9:
            res.append('IX')
            num -= 9
        elif num >= 5:
            res.append('V')
            num -= 5
        elif num >= 4:
            res.append('IV')
            num -= 4
        else:
            count = num
            res.append(count * 'I')
            num -= count * 1
    return ''.join(res)


def intToRoman2(num: int) -> str:
    table = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC',
            50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
    res = []
    for n, s in table.items():
        count = num // n
        res.append(count * s)
        num -= count * n
        if num == 0:
            break
    return ''.join(res)