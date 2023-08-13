## https://leetcode.com/problems/keyboard-row/

keyboard = { 1 : ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                2 : ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                3 : ['z', 'x', 'c', 'v', 'b', 'n', 'm'] }

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ans = words[:]
        for word_o in words :
            word = word_o.lower()
            for k, v in keyboard.items() :
                if word[0] in v : break
            for w in word :
                if w not in keyboard[k] :
                    ans.remove(word_o)
                    break
        return ans