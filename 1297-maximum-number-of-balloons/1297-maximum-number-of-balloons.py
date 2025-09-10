class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import Counter
        freq=Counter(text)
        count=0
        if 'b' in freq and 'a' in freq and 'l' in freq and 'o' in freq and 'n' in freq:
            while freq['b']>0 and freq['a']>0 and freq['l']>1 and freq['n']>0 and freq['o']>1:
                count+=1
                freq['b']-=1
                freq['a']-=1
                freq['l']-=2
                freq['o']-=2
                freq['n']-=1
            return count 
        return 0
        