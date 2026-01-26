## https://leetcode.com/problems/count-vowel-substrings-of-a-string/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans, ln, v = 0, len(word), set(["a", "e", "i", "o", "u"])
        for i in range(ln - 4):
            if word[i] in v:
                for j in range(i + 5, ln + 1):
                    if word[j - 1] not in v: break
                    if set(word[i:j]) == v: ans += 1
        return ans