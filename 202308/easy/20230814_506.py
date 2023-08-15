## https://leetcode.com/problems/relative-ranks/

class Solution(object):
    def findRelativeRanks(self, score):
        """
        :type score: List[int]
        :rtype: List[str]
        """
        sorted_score = sorted(score, reverse=True)
        ans = []
        for s in score :
            tmp = sorted_score.index(s)
            if tmp == 0 : ans.append("Gold Medal")
            elif tmp == 1 : ans.append("Silver Medal")
            elif tmp == 2 : ans.append("Bronze Medal")
            else : ans.append(str(tmp+1))
        
        return ans