## https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        s = ""
        for num in nums : s += str(num)
        lst = s.strip("0").split("1")
        for l in lst[1:-1] :
            if len(l) < k : return False
        return True