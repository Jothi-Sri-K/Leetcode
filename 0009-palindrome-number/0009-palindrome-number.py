class Solution:
    def isPalindrome(self, x: int) -> bool:
        #return str(x)==str(x)[::-1]
        org=x
        rev=0
        while (x>0):
            last=x%10
            rev=(rev*10)+last
            x=x//10
        return org==rev


        


        