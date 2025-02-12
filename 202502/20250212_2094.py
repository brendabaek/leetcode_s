## https://leetcode.com/problems/finding-3-digit-even-numbers/

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ln, ans = len(digits), set()
        for i in range(ln) :
            if digits[i] == 0 : continue
            for j in range(ln) :
                if i == j : continue
                for k in range(ln) :
                    if i == k or j == k : continue
                    if digits[k] % 2 == 1 : continue
                    ans.add(digits[i]*100 + digits[j]*10 + digits[k])
        return sorted(list(ans))