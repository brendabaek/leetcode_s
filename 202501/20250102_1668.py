## https://leetcode.com/problems/maximum-repeating-substring/

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        if sequence == None or word == None : return False
        w, cnt = word, 0
        while w in sequence :
            cnt += 1
            w = w + word
        return cnt