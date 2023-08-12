## https://leetcode.com/problems/construct-the-rectangle/

class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        a, l, w = area, 1, 1
        for i in range(1, int((area**0.5)+1)) :
            if area % i == 0 and (i * (area/i)) <= a :
                if (area/i) < i : return [l, w]
                a, l, w = (i * (area/i)), (area/i), i
        return [l, w]
                