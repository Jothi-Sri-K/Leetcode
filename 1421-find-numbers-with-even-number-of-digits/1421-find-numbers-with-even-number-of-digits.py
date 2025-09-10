class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        
        for num in nums:
            number_of_digits=len(str(num))
            if number_of_digits%2==0:
                count+=1
        return count