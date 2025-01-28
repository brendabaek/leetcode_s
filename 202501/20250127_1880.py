## https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return self.nums(firstWord) + self.nums(secondWord) == self.nums(targetWord)

    def nums(self, letters) :
        v = 0
        for letter in letters : v = (v * 10) + ord(letter) - 97
        return v