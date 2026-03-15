class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s=list(s)
        left=0
        right=len(s)-1
        moves=0
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
                continue
            k=right
            while k>left and s[k]!=s[left]:
                k-=1
            if k==left:
                s[left],s[left+1]=s[left+1],s[left]
                moves+=1
            else:
                while k<right:
                    s[k],s[k+1]=s[k+1],s[k]
                    moves+=1
                    k+=1
                    
                left+=1
                right-=1
        return moves