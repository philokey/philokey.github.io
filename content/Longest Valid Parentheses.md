Title: Longest Valid Parentheses @ LeetCode
Date: 2014-08-14 10:02
Category: LeetCode
Tags: stack

题意： 给出括号序列，问最长的连续合法括号子序列长度是多少

解法：用一个栈记录左括号, 右括号和在数组中的下标, 如果当前括号是右括号且栈顶是左括号, 则弹栈并更新答案
```
class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        sLen, stack, ret = len(s), [(-1, ')')], 0
        for i in range(sLen):
            if stack[-1][1] == '(' and s[i] == ')':
                stack.pop()
                ret = max(ret, i - stack[-1][0])
            else :
                stack.append((i, s[i]))
        return ret
```


> Written with [StackEdit](https://stackedit.io/).
