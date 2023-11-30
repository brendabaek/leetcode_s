## https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        for des in paths :
            d = des[1]
            check = True
            for p in paths :
                s = p[0]
                if s == d :
                    check = False
                    break
            if check == True : return d