class Solution:
    def countDigits(self, num: int) -> int:
        num_cpy=list(str(num))
        count=0
        for nums in num_cpy:
            if (num%(int(nums)))==0:
                count+=1
        return count

        