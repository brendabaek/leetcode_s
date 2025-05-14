## https://leetcode.com/problems/unique-3-digit-even-numbers/

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ln, ans = len(digits), set()
        for i in range(ln):
            for j in range(ln):
                for k in range(ln):
                    if i == j or j == k or i == k: continue
                    if digits[i] != 0 and digits[k] % 2 == 0:
                        ans.add((digits[i] * 100) + (digits[j] * 10) + digits[k])
        return len(ans)