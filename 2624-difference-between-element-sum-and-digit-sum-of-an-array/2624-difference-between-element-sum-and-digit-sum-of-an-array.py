class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum=0
        digit_sum=0
        for num in nums:
            element_sum+=num
            num_cpy=list(str(num))
            for i in range(0,len(num_cpy)):
                digit_sum+=int(num_cpy[i])
        return abs(element_sum-digit_sum)
