## https://leetcode.com/problems/path-crossing/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        points, w, l = [(0, 0)], 0, 0
        for p in path :
            if p == "N" : l += 1
            elif p == "S" : l -= 1
            elif p == "E" : w += 1
            else : w -= 1
            if (w, l) in points : return True
            else : points.append((w, l))
        return False