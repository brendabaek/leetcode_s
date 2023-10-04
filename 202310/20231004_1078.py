## https://leetcode.com/problems/occurrences-after-bigram/

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        lst = text.split(' ')
        idx, ans, ln = 0, [], len(lst)
        while idx < ln-2 :
          if lst[idx] == first and lst[idx+1] == second : ans.append(lst[idx+2])
          idx += 1
        return ans
