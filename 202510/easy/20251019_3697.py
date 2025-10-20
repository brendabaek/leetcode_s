## https://leetcode.com/problems/compute-decimal-representation/

class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        cnt, ans = 0, []
        while n > 0:
            tmp = ((n % 10) * (10 ** cnt))
            if tmp != 0: ans = [tmp] + ans
            n //= 10
            cnt += 1
        return ans