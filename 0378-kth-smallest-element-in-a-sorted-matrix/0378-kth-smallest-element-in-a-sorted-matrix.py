class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst=[item for row in matrix for item in row]
        lst.sort()
        return lst[k-1]
        