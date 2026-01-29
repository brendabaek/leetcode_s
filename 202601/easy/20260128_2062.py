## https://leetcode.com/problems/count-vowel-substrings-of-a-string/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans, ln, v = 0, len(word), set(["a", "e", "i", "o", "u"])
        s, e = 0, 0
        while s < ln - 4 and e <= ln:
            if word[s] not in v: s, e = s + 1, e + 1
            else:
                if e - s < 5:
                    if e == ln: return ans
                    if word[e] in v: e += 1
                    else: s, e = e + 1, e + 1
                else:
                    if set(word[s:e]) == v: ans += 1
                    if e < ln and word[e] in v: e += 1
                    else: s, e = s + 1, min(s + 5, e)
        return ans