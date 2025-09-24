class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_count=0
        for sentence in sentences:
            max_count=max(max_count,len(sentence.split()))
        return max_count
        
        