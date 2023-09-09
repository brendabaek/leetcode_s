## https://leetcode.com/problems/most-common-word/

import re
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        remove_lst = ['!', '?', '\'', ',', ';', '.']
        for r in remove_lst :
            paragraph = paragraph.replace(r, ' ')
            paragraph = paragraph.replace('  ', ' ')
        paragraph = ''.join(re.findall(r'[a-zA-Z ]', paragraph.lower())).split(' ')
        dics = {}
        for p in paragraph :
            if p not in banned and len(p) > 0 :
                try : dics[p] += 1
                except : dics[p] = 1
        return max(dics, key=dics.get)