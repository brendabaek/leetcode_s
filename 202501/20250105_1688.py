## https://leetcode.com/problems/count-of-matches-in-tournament/

class Solution:
    def numberOfMatches(self, n: int) -> int:
        cnt = 0
        while n > 1 :
            if n % 2 == 1 :
                n = n // 2
                cnt += n + 1
            else :
                n = n //2
                cnt += n
        return cnt