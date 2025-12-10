import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set=set(banned)
        words=re.findall(r"[a-zA-Z]+",paragraph.lower())
        count=Counter()
        
        for w in words:    
            if w not in banned_set:
                count[w]+=1
        return count.most_common(1)[0][0]