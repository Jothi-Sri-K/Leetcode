class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        currentsum=0
        prefixsums={0:1}

        for n in nums:
            currentsum+=n
            diff=currentsum-k
            res+=prefixsums.get(diff,0)
            prefixsums[currentsum]=1+prefixsums.get(currentsum,0)
        return res