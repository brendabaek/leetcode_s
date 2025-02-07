## https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try : idx = word.index(ch)
        except : return word
        return word[idx::-1] + word[idx+1:]