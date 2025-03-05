## https://leetcode.com/problems/check-distances-between-same-letters/

class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        # n, dics = 0, {}
        # for l in s :
        #     try : dics[l].append(n)
        #     except : dics[l] = [n]
        #     n += 1
        # for k, v in dics.items() :
        #     if distance[ord(k)-97] != v[1] - v[0] - 1 : return False
        # return True

        n, p = 0, [0 for _ in range(26)]
        for l in s :
            idx = ord(l)-97
            if p[idx] == 0 : p[idx] = n+1
            else :
                if n - p[idx] != distance[idx] : return False
            n += 1
        return True