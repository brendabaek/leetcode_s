## https://leetcode.com/problems/button-with-longest-push-time/

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        dics = {events[0][1]: [events[0][0]]}
        for i in range(1, len(events)):
            try: dics[events[i][1] - events[i-1][1]].append(events[i][0])
            except: dics[events[i][1] - events[i-1][1]] = [events[i][0]]
        return min(dics[max(dics)])

        # t, ans = events[0][1], events[0][0]
        # for i in range(1, len(events)):
        #     if events[i][1] - events[i-1][1] > t: t = events[i][1] - events[i-1][1]; ans = events[i][0]
        #     elif events[i][1] - events[i-1][1] == t: ans = min(ans, events[i][0])
        # return ans

        # p, t, ans = events[0][1], events[0][1], events[0][0]
        # for e in events[1:]:
        #     if e[1] - p > t: t = e[1] - p; ans = e[0]
        #     elif e[1] - p == t: ans = min(ans, e[0])
        #     p = e[1]
        # return ans