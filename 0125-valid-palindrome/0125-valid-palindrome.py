class Solution:
    def isPalindrome(self, s: str) -> bool:
        str2=""
        length=len(s)
        
        for i in range(0,length):
            if s[i].isalnum():
                str2=str2+s[i]
        str2=str2.lower()
        first=0
        last=len(str2)-1
        while first<last:
            if str2[first]==str2[last]:
                first+=1
                last-=1
            else:
                return False
        return True

