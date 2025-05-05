## https://leetcode.com/problems/check-balanced-string/

class Solution:
    def isBalanced(self, num: str) -> bool:
        check, ans = True, 0
        for i in range(len(num)):
            if check == True: ans += int(num[i]); check = False
            else: ans -= int(num[i]); check = True
        return ans == 0