class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        negative = num < 0
        num = abs(num)
        digits = []
        while num > 0:
            r = num % 7
            digits.append(str(r))
            num //= 7
        result = ''.join(reversed(digits))
        return "-" + result if negative else result
