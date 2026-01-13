class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_2=0
        prev_1=0
        for num in nums:
            current=max(prev_1,prev_2+num)
            prev_2=prev_1
            prev_1=current
        return prev_1
        
            
        