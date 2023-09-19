## https://leetcode.com/problems/reverse-only-letters/

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        idx1, idx2 = 0, len(s)-1
        while idx1 < idx2 :
            ord1, ord2 = ord(s[idx1]), ord(s[idx2])
            if ((65 <= ord1 and ord1 <= 90) or (97 <= ord1 and ord1 <= 122)) and \
                ((65 <= ord2 and ord2 <= 90) or (97 <= ord2 and ord2 <= 122)) :
                s = s[:idx1] + s[idx2] + s[idx1+1:idx2] + s[idx1] + s[idx2+1:]
                idx1 += 1
                idx2 -= 1
            elif not ((65 <= ord1 and ord1 <= 90) or (97 <= ord1 and ord1 <= 122)) : idx1 += 1
            elif not ((65 <= ord2 and ord2 <= 90) or (97 <= ord2 and ord2 <= 122)) : idx2 -= 1
            else :
                idx1 += 1
                idx2 -= 1
        return s