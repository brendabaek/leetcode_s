## https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution:
    def minMaxDifference(self, num: int) -> int:
        num, max_num = str(num), str(num)
        if set(num) == set('9') : pass
        else :
            for n in num :
                if n != '9' : max_num = num.replace(n, '9'); break
        min_num = num.replace(num[0], '0')
        return int(max_num) - int(min_num)