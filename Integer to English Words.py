# https://leetcode.com/problems/integer-to-english-words/description/


# TC:O(N) N digits, SC:O(1)
def numberToWords(num: int) -> str:
    # 31*0.3 = 9.3, 10^9:billion, 10^6: million, thousand, hundred
    if num == 0:
        return 'Zero'

    def convert(num):
        # if num == 0: return ''
        if 1 <= num <= 9:
            one = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
                   6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
            return one[num]
        elif 10 <= num <= 19:
            two = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen',
                   14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
                   18: 'Eighteen', 19: 'Nineteen'}
            return two[num]
        elif 20 <= num <= 99:
            three = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty',
                     6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
            digit = num // 10
            num %= 10
            if num:
                return three[digit] + ' ' + convert(num)
            return three[digit]
        else:
            hundred = num // 100
            num %= 100
            if num:
                return convert(hundred) + ' Hundred ' + convert(num)
            return convert(hundred) + ' Hundred'

    res = ''
    billion = num // 1000000000
    num %= 1000000000
    if billion:
        res += convert(billion) + ' Billion'
    million = num // 1000000
    num %= 1000000
    if million:
        res += (' ' if res else '') + convert(million) + ' Million'
    thousand = num // 1000
    num %= 1000
    if thousand:
        res += (' ' if res else '') + convert(thousand) + ' Thousand'
    if num:
        res += (' ' if res else '') + convert(num)
    return res