class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        expected_sum=(n*(n+1))//2
        original_sum=sum(nums)
        return expected_sum-original_sum
        