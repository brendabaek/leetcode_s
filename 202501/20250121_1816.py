## https://leetcode.com/problems/truncate-sentence/

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        ans = ""
        for i in s :
            if k == 1 :
                if i == " " : return ans
            else :
                if i == " " : k -= 1
            ans += i
        return ans