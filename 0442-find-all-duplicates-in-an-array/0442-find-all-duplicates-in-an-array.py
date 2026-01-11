class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        res=[]
        count=1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                count+=1
            if count==2:
                res.append(nums[i])
                count=1
        return res
            
       
        