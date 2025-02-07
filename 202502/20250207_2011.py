## https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans = 0
        for o in operations : ans += 1 if o[1] == '+' else -1
        return ans