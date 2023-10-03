## https://leetcode.com/problems/greatest-common-divisor-of-strings/

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1 : return ''
        if len(str1) < len(str2) : str1, str2 = str2, str1
        ln1, ln2 = len(str1), len(str2)
        for i in range(ln2, 0, -1) :
            if ln1 % i == 0 and ln2 % i == 0 : return str2[:i]
        return ''