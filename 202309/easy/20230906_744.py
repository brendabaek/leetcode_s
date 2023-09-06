## https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        t = ord(target)
        for l in letters :
            if ord(l) > t : return l
        return letters[0]