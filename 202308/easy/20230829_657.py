## https://leetcode.com/problems/robot-return-to-origin/

class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        dics = {'R':0, 'L':0, 'U':0, 'D':0}
        for m in moves : dics[m] += 1

        if dics['R'] - dics['L'] == 0 and dics['U'] - dics['D'] == 0 : return True
        else : return False