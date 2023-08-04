## https://leetcode.com/problems/ransom-note/

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        for l in ransomNote :
            if l in magazine :
                magazine = magazine.replace(l, '', 1)
            else : return False

        return True