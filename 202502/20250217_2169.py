## https://leetcode.com/problems/count-operations-to-obtain-zero/

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ans = 0
        if num1 == 0 or num2 == 0 : return 0
        if num1 == num2: return 1
        while num1 != num2 and num1 != 0 and num2 != 0 :
            num1, num2 = max(num1, num2), min(num1, num2)
            ans += num1 // num2
            num1 = num1 % num2            
        return ans