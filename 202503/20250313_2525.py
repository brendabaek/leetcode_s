## https://leetcode.com/problems/categorize-box-according-to-criteria/

class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        if length >= 10000 or width >= 10000 or height >= 10000 or (length * width * height) >= 10 ** 9 :
            return "Both" if mass >= 100 else "Bulky"
        else : return "Heavy" if mass >= 100 else "Neither"