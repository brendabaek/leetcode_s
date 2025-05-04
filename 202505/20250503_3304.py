## https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = 0
        while k > 1:
            r = 0
            while 2 ** r <= k: r += 1
            ans += 1
            if 2 ** (r - 1) == k: k = k // 2
            else: k = k % (2 ** (r - 1))
        return chr(ans + 97)

        # r, ans = 0, [0]
        # while 2 ** r <= k: r += 1
        # for i in range(r):
        #     for a in ans.copy(): ans.append(a + 1)
        # return chr(ans[k - 1] % 26 + 97)

        # r, ans = 0, "a"
        # while 2 ** r <= k: r += 1
        # for i in range(r):
        #     for a in ans: ans += chr(((ord(a) - 96) % 26) + 97)
        # return ans[k - 1]