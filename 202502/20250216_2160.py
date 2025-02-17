## https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/

class Solution:
    def minimumSum(self, num: int) -> int:
        lst = []
        while num > 0 :
            lst.append(num % 10)
            num //= 10
        new1 = min(lst) * 10 + max(lst)
        lst.remove(min(lst)), lst.remove(max(lst))
        new2 = min(lst) * 10 + max(lst)
        return new1 + new2