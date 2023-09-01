## https://leetcode.com/problems/baseball-game/

class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ans = []
        for o in operations :
            if o == '+' : ans.append(ans[-1]+ans[-2])
            elif o == 'D' : ans.append(ans[-1]*2)
            elif o == 'C' : ans.pop()
            else : ans.append(int(o))
        return sum(ans)