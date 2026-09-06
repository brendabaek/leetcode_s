## https://leetcode.com/problems/find-the-degree-of-each-vertex/

class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        return [m.count(1) for m in matrix]