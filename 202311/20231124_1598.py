## https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        cnt = 0
        for l in logs :
            if l == "../" : cnt = max(0, cnt-1)
            elif l == "./" : pass
            else : cnt += 1
        return cnt