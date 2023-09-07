## https://leetcode.com/problems/shortest-completing-word/

import re
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        letter = ''.join(re.findall(r'[a-zA-Z]', licensePlate.replace(' ', ''))).lower()
        for word in words :
            w, check = word, True
            for l in letter :
                if l in w : w = w.replace(l, '', 1)
                else :
                    check = False;  break
            if check == True :
                try :
                    if len(word) < len(ans) : ans = word
                except : ans = word
        return ans