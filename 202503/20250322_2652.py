## https://leetcode.com/problems/sum-multiples/

s, ans = 0, []
for i in range(1001) :
    for j in [3, 5, 7] :
        if i % j == 0 : s += i; break
    ans.append(s)

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        return ans[n]
        # ans = 0
        # for i in range(n+1) :
        #     if i % 3 == 0 or i % 5 == 0 or i % 7 == 0 : ans += i
        # return ans