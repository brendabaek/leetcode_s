## https://leetcode.com/problems/find-valid-pair-of-adjacent-digits-in-string/

class Solution:
    def findValidPair(self, s: str) -> str:
        a = ""
        for i in set(s):
            if int(i) == s.count(i): a += i
        for j in range(len(s) - 1):
            if s[j] != s[j + 1] and s[j] in a and s[j + 1] in a: return s[j:j + 2]
        return ""

        # dics = {}
        # for i in s:
        #     try: dics[i] += 1
        #     except: dics[i] = 1
        # for j in range(len(s) - 1):
        #     if s[j] != s[j + 1] and dics[s[j]] == int(s[j]) and dics[s[j + 1]] == int(s[j + 1]): return s[j:j + 2]
        # return ""