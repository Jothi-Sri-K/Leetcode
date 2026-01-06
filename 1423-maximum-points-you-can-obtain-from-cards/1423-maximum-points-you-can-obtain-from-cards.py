class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum1=sum(cardPoints[:k])
        l,r=k-1,len(cardPoints)-1
        max_sum=sum1
        cur_sum=sum1
        for i in range(0,k):
            cur_sum-=cardPoints[l]
            cur_sum+=cardPoints[r]
            l-=1
            r-=1
            max_sum=max(cur_sum,max_sum)
        return max_sum