class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """My first approach with time complexity O(nlogn)
        nums.sort()
        res=[]
        count=1
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                count+=1
            else:
                count=1
            if count==2:
                res.append(nums[i])
                count=1
        return res"""

        res=[]
        for i in range(len(nums)):
            index=abs(nums[i])-1
            if nums[index]<0:
                res.append(abs(nums[i]))
            else:
                nums[index]=-nums[index]
        return res

            
       
        