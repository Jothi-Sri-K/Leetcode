class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        
        for num in nums:
            number_of_digits=0
            for digit in str(num):
                number_of_digits+=1
            if number_of_digits%2==0:
                count+=1
        return count