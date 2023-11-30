## https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        ln, cnt, lst = len(searchWord), 1, sentence.split(" ")
        for l in lst :
            if searchWord == l[:ln] : return cnt
            else : cnt += 1
        return -1