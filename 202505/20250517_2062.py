## https://leetcode.com/problems/count-vowel-substrings-of-a-string/

class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        s, e, ans, ln, l = -1, 1, 0, len(word), "aeiou"
        if len(set(word)) < 5: return 0
        for idx1 in range(ln):
            if word[idx1] in l: s = idx1; break
        if s == -1: return 0
        while s < ln - 4 and e < ln:
            if word[e] not in l:
                if e >= ln - 1: break
                for idx2 in range(e+1, ln):
                    s = idx2
                    if word[idx2] in l: break
                e = s + 1; continue
            else:
                if e - s >= 4:
                    for i in range(s, e-3):
                        if len(set(word[i:e+1])) == 5: ans += 1
                        else: break
                e += 1
        return ans