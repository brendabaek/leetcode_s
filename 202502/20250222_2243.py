## https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k :
            tmp = ""
            for i in range(0, len(s), k) :
                nums, sums = s[i:i+k], 0
                for num in nums : sums += int(num)
                tmp += str(sums)
            s = tmp
        return s