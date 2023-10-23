## https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        if '6' not in s : return num
        else : return int(s.replace('6', '9', 1))