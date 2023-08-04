## https://leetcode.com/problems/zigzag-conversion/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 : return s
        lst = [[] for _ in range(numRows)]
        r, c = 0, 0

        for l in s :
            if (r < numRows) and (c % (numRows-1) == 0) :
                lst[r].append(l)
                if r < (numRows-1) : r += 1
                else :
                    r -= 1
                    c += 1
                
            else :
                lst[r].append(l)
                r -= 1
                c += 1

        ans = ''.join([''.join(i) for i in lst])
        return ans