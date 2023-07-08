## https://leetcode.com/problems/excel-sheet-column-number/

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        if columnTitle == None or columnTitle == 0 : return
        ln = len(columnTitle)
        ans = 0
        cnt = 0
        for i in range(ln-1, -1, -1) :
            ans += (ord(columnTitle[i]) - 64) * (26 ** cnt)
            cnt += 1
        return ans