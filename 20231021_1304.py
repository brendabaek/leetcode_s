## https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        num, ans = 1, []
        for i in range(1, (n//2)+1) : ans += [i, -i]
        if n % 2 == 1 : ans += [0]
        return ans