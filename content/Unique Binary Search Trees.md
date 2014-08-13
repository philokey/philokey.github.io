Title: Unique Binary Search Trees @ LeetCode
Date: 2014-08-13 23:20
Category: LeetCode
Tags: dp
题意：给定 1-n 共n个数， 问可以组成多少种不同的二分查找树。

解法：动态规划。

dp[n] 表示有n个数时，构成不同二分查找树的个数。转移方程为：
$$
dp[n] = \sum_{i=0}^{n-1}dp[i]*dp[n-i-1]
$$
```
class Solution:
    # @return an integer
    def numTrees(self, n):
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(1,n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[n]
```
