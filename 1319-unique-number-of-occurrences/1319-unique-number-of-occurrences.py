class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        from collections import Counter
        freq={}
        freq=Counter(arr)
        occurrences = list(freq.values())
        if len(set(occurrences))==len(occurrences):
            return True
        return False