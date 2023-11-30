## https://leetcode.com/problems/most-visited-sector-in-a-circular-track/

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        s, e = rounds[0], rounds[-1]
        if s == e : return [s]
        elif s < e : return [i for i in range(s, e+1)]
        else : return [i for i in range(1, e+1)] + [i for i in range(s, n+1)]