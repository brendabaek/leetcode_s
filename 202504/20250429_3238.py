## https://leetcode.com/problems/find-the-number-of-winning-players/

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        # ctr, ans = Counter(map(tuple, pick)), set()
        # for (a, b), c in ctr.items():
        #     if a < c: ans.add(a)
        # return len(ans)

        dics, ans = {}, 0
        for p in pick:
            try: dics[p[0]].append(p[1])
            except: dics[p[0]] = [p[1]]
        for k, v in dics.items():
            set_lst = set(v)
            for s in set_lst:
                if v.count(s) > k: ans += 1; break
        return ans