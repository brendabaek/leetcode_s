## https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        while s != "" :
            if words == [] or s[:len(words[0])] != words[0] : return False
            else :
                s = s[len(words[0]):]
                words.pop(0)
        return True