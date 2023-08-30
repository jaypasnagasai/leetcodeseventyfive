#547. Number of Provinces

class Solution:
    def findCircleNum(self, isConnected):
        N = len(isConnected)
        visited = set()
        def dfs(cityI):
            cityIConnections = isConnected[cityI]
            visited.add(cityI)
            for cityJ in range(N):
                if (cityJ not in visited) and (cityIConnections[cityJ] == 1) and (cityI != cityJ):
                    dfs(cityJ)
            return 
        numProvinces = 0
        for cityI in range(N):
            if cityI not in visited:
                dfs(cityI)
                numProvinces += 1
        return numProvinces
