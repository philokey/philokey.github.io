Title: Search in Rotated Sorted Array 
Date: 2014-08-16 11:20
Category: LeetCode
Tags: binary search

解法：二分法，分别讨论左边单调递增还是右边单调递增。当有重复元素时， A[l] == A[m] 的情况要单独拿出来考虑， 因为有[l,m] => [1,3,1]这种情况

```
class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        l, r = 0, len(A) - 1
        while l <= r:
            m = (l + r) / 2
            if A[m] == target: return True
            if A[l] < A[m]:
                if A[l] <= target < A[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif A[l] > A[m]:
                if A[m] < target <= A[r]:
                    l = m + 1
                else:
                    r = m - 1
            else :
                l += 1
        return False
```
