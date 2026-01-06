class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        rcount,wcount,bcount=0,0,0
        for i in range(0,len(nums)):
            if nums[i]==0:
                rcount+=1
            elif nums[i]==1:
                wcount+=1
            else:
                bcount+=1
        nums[:rcount]=[0]*rcount
        nums[rcount:rcount+wcount]=[1]*wcount
        nums[wcount+rcount:]=[2]*bcount        
        
        
        
        