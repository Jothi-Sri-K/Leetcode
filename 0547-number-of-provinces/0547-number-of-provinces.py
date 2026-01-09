class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        vis=[0]*n

        def dfs(city):
            vis[city]=1
            for i in range(n):
                if isConnected[city][i]==1 and vis[i]==0:
                    dfs(i)
        
        provinces=0
        for i in range(n):
            if vis[i]==0:
                provinces+=1
                dfs(i)
        return (provinces)


