## https://leetcode.com/problems/count-integers-with-even-digit-sum/

lst = []
for i in range(1, 1001) :
    n, s = i, 0
    while n > 0 :
        s += n % 10
        n = n // 10
    if s % 2 == 0 : lst.append(i)

class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for l in lst :
            if l <= num : ans += 1
            else : return ans; break
        return ans