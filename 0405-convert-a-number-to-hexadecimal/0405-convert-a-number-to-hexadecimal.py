class Solution:
    def toHex(self, num: int) -> str:
        num &= 0xFFFFFFFF
        return hex(num)[2:]