## https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0 : return 0
        else : ans = -1
        while num > 0 :
            if num % 2 == 1 : ans += 1
            num = num // 2
            ans += 1
        return ans