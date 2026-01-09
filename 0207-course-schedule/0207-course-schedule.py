from collections import deque

class Solution:
    def canFinish(self, n, prerequisites):
        adj = [[] for _ in range(n)]
        for course, pre in prerequisites:
            adj[pre].append(course)
        indeg = [0] * n
        for i in range(n):
            for j in adj[i]:
                indeg[j] += 1
        q = deque()
        for i in range(n):
            if indeg[i] == 0:
                q.append(i)

        topo = []

        while q:
            node = q.popleft()
            topo.append(node)

            for nei in adj[node]:   
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
        return len(topo) == n
