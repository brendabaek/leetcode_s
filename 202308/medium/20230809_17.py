## https://leetcode.com/problems/letter-combinations-of-a-phone-number/

disc = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j', 'k', 'l'],
        '6':['m', 'n', 'o'], '7':['p', 'q', 'r', 's'], '8':['t', 'u', 'v'], '9':['w', 'x', 'y', 'z']}

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "" : return
        digits = [disc[n] for n in digits]
        return self.make_ans(digits, 0, len(digits))

    def make_ans(self, digits, cnt, ln) :
        cnt += 1
        s, ans = [], []
        if cnt < ln : s = self.make_ans(digits[1:], cnt, ln)
        if s == [] :
            for l in digits : s.append(l)
            return s[0]
        else :
            for l in digits[0] :
                for m in s : ans.append(l+m)
            return ans