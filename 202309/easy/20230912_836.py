## https://leetcode.com/problems/rectangle-overlap/

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        for _ in range(2) :
            if ((rec2[0] <= rec1[0]) and (rec1[0] < rec2[2])) and \
                (((rec2[1] <= rec1[1]) and (rec1[1] < rec2[3])) or \
                ((rec2[1] <= rec1[3]) and (rec1[3] < rec2[3]))) :
                return True
            if ((rec2[0] <= rec1[0] and rec1[0] <= rec2[2])) and \
                ((rec2[0] <= rec1[2] and rec1[2] <= rec2[2])) and \
                ((rec1[1] <= rec2[1] and rec2[3] <= rec1[3])) :
                return True
            rec1, rec2 = rec2, rec1
        return False
