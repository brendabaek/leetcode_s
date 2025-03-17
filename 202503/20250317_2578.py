## https://leetcode.com/problems/split-with-minimum-sum/

class Solution:
    def splitNum(self, num: int) -> int:
        lst = [n for n in str(num)]
        lst.sort()
        n1, n2 = "", ""
        while lst != [] :
            n1 += lst.pop(0)
            if lst != [] : n2 += lst.pop(0)
        return int(n1) + int(n2)