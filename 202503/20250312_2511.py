## https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

class Solution:
    def captureForts(self, forts: List[int]) -> int:
        idx, ln, check, dist, ans = 1, len(forts), forts[0], 0, 0
        while idx < ln :
            if check == 0 : check = forts[idx]
            elif check == 1 :
                if forts[idx] == 0 : dist += 1
                elif forts[idx] == 1 : dist = 0
                else : ans = max(ans, dist); check = forts[idx]; dist = 0;
            elif check == -1 :
                if forts[idx] == 0 : dist += 1
                elif forts[idx] == -1 : dist = 0
                else : ans = max(ans, dist); check = forts[idx]; dist = 0;
            idx += 1
        return ans