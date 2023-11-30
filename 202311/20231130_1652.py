## https://leetcode.com/problems/defuse-the-bomb/

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ln = len(code)
        if k == 0 : return [0 for _ in range(ln)]
        elif k > 0 :
            code = code + code[:k]
            return [sum(code[i+1:i+1+k]) for i in range(ln)]
        else :
            code = code[k:] + code
            return [sum(code[i:i-k])for i in range(ln)]