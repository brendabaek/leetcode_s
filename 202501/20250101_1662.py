## https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1 = ''
        for i in word1 :
            for j in i :
               w1 = w1 + j
        for i in word2 :
            for j in i :
                try :
                    if j == w1[0] :
                        try : w1 = w1[1:]
                        except : return False
                    else : return False
                except : return False
        if w1 == '' : return True
        else : return False