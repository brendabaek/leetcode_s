## https://leetcode.com/problems/count-the-number-of-vowel-strings-in-range/

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        cnt, lst = 0, ['a', 'e', 'i', 'o', 'u']
        for word in words[left:right+1] :
            if word[0] in lst and word[-1] in lst : cnt += 1
        return cnt