class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        freq=Counter(arr)
        res=[]
        for key,value in freq.items():
            if key==value:
                res.append(key)
        if res:
            return max(res)
        else:
            return -1        
        