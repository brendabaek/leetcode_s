## https://leetcode.com/problems/excel-sheet-column-title/

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        if columnNumber == None or columnNumber == 0 : return

        lst = []
        ans = []

        while columnNumber > 26 :
            if columnNumber % 26 == 0 :
                lst.append(26)
                columnNumber -= 26
            else :
                lst.append(columnNumber % 26)
            columnNumber //= 26
        lst.append(columnNumber)

        for i in range(len(lst)-1, -1, -1) :
            ans.append(chr(lst[i]+64))

        return ''.join(ans)