class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum=0
        prod=1
        for digit in str(n):
            sum+=int(digit)
            prod*=int(digit)
        return prod-sum
