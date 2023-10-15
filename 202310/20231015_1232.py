## https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        ln, l, r = len(coordinates), [], []
        for i in range(1, ln) :
            l.append(coordinates[i][0] - coordinates[i-1][0])
            r.append(coordinates[i][1] - coordinates[i-1][1])
        if l == [0] * (ln-1) or r == [0] * (ln-1) : return True
        elif 0 in l or 0 in r : return False
        check = l[0]/r[0]
        for j in range(1, ln-1) :
            if l[j]/r[j] != check : return False
        return True
    
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(1, len(coordinates)) :
            x, y = coordinates[i]
            if (x1 - x0) * (y - y1) != (y1 - y0) * (x - x1) :
                return False