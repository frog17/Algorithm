class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1)+1, len(word2)+1
        dis = [[0 for i in range(l2)] for i in range(l1)]
        
        for i in range(l1):
            dis[i][0] = i
        for j in range(l2):
            dis[0][j] = j
        for i in range(1, l1):
            for j in range(1, l2):
                dis[i][j] = min(dis[i-1][j]+1, dis[i][j-1]+1, dis[i-1][j-1]+(word1[i-1] != word2[j-1]))
        
        return dis[-1][-1]
