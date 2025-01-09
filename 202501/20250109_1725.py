## https://leetcode.com/problems/number-of-rectangles-that-can-form-the-largest-square/

class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        cnt, m_ln = 0, 0
        for r in rectangles :
            if m_ln == min(r) : cnt += 1
            elif m_ln < min(r) :
                cnt = 1
                m_ln = min(r)
        return cnt