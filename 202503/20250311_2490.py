## https://leetcode.com/problems/circular-sentence/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1] : return False
        words = sentence.split(" ")
        l = words[0][-1]
        for word in words[1:] :
            if word[0] != l : return False
            l = word[-1]
        return True