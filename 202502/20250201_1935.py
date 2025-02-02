## https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text = text.split()
        ans = 0
        for t in text :
            check = True
            for i in t :
                if i in brokenLetters :
                    check = False
                    break
            if check == True : ans += 1
        return ans