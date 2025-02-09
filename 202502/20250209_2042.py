## https://leetcode.com/problems/check-if-numbers-are-ascending-in-a-sentence/

class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = s.split(" ")
        lst = []
        for l in s :
            try : lst.append(int(l))
            except : pass
        tmp = 0
        for n in lst :
            if n <= tmp : return False
            tmp = n
        return True