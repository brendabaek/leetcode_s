## https://leetcode.com/problems/detect-capital/

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.upper() : return True
        elif word == word.lower() : return True
        elif word == word[0].upper()+word[1:].lower() : return True
        else : return False