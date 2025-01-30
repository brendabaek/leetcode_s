## https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dics = {}
        for word in words :
            for w in word :
                try : dics[w] += 1
                except : dics[w] = 1
        ln = len(words)
        for v in dics.values() :
            if v % ln != 0 : return False
        return True