## https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        word = s
        for l in word :
            ln1 = len(word)
            word = word.replace(l, '')
            ln2 = len(word)

            if (ln1-1) == ln2 :
                return s.index(l)

        return -1
