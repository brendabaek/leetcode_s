## https://leetcode.com/problems/student-attendance-record-i/

class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return len(s.replace("LLL", '').replace("A", '')) > len(s)-2