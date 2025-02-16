## https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ln, ans = len(s), []
        if ln % k != 0 :
            s = s + (fill * (k - (ln % k)))
            return [s[i * k:(i + 1) * k] for i in range(ln // k + 1)]
        else : return [s[i * k:(i + 1) * k] for i in range(ln // k)]