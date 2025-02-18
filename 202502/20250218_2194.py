## https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        s1, e1 = ord(s[0]), ord(s[-2])
        s2, e2 = ord(s[1]), ord(s[-1])
        ans = []
        for i in range(s1, e1+1) :
            for j in range(s2, e2+1) :
                ans.append(chr(i)+chr(j))
        return ans