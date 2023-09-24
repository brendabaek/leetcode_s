## https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for i in range(len(words)-1) :
            if words[i] == words[i+1] or words[i] == words[i+1][:len(words[i])] : pass
            else :
                cnt = 0
                while cnt < len(words[i]) and cnt < len(words[i+1]) :
                    if words[i][cnt] == words[i+1][cnt] : cnt += 1
                    else : break
                if cnt == min(len(words[i]), len(words[i+1])) and len(words[i]) > len(words[i+1]) : return False
                try :
                    if order.index(words[i][cnt]) > order.index(words[i+1][cnt]) : return False
                except : return False
        return True