## https://leetcode.com/problems/number-of-even-and-odd-bits/

class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        b, e, o = bin(n)[2:], 0, 0
        for i in range(1, len(b)+1) :
            if i % 2 == 0 and b[-i] == "1" : e += 1
            elif i % 2 == 1 and b[-i] == "1" : o += 1
        return [o, e]