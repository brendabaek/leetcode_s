## https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/

class Solution:
    def largestInteger(self, num: int) -> int:
        num, even, odd, check, ans = str(num), [], [], [], ""
        for n in num :
            if int(n) % 2 == 0 : even.append(n); check.append(0)
            else : odd.append(n); check.append(1)
        even.sort(), odd.sort()
        for c in check : ans += even.pop() if c == 0 else odd.pop()
        return int(ans)