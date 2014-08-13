Title: Unique Paths II @ LeetCode
Date: 2014-08-14 00:20
Category: LeetCode
Tags: dp
题意：给n*m的格子，1有障碍物，0表示没有障碍物，问从左上角到右下角有几种走法，其中有障碍物的格子不能通过。
解法：
动态规划。
初始化第一行和第一列时遇到障碍物就停止
dp[i][j] = dp[i-1][j] + dp[i][j-1], 如果grid[i][j]有障碍物, dp[i][j] = 0
 
```
class Solution:
	# @param obstacleGrid, a list of lists of integers
	# @return an integer
	def uniquePathsWithObstacles(self, obstacleGrid):
		n, m = len(obstacleGrid), len(obstacleGrid[0])
		dp =[[0 for j in range(m)] for i in range(n)]
		for i in range(n):
			if obstacleGrid[i][0] == 1: break
			dp[i][0] = 1
		for i in range(m):
			if obstacleGrid[0][i] == 1: break
			dp[0][i] = 1
		for i in range(1,n):
			for j in range(1,m):
				if obstacleGrid[i][j] == 0:
					dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
		return dp[n - 1][m - 1]

```
