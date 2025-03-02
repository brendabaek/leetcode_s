## https://leetcode.com/problems/merge-similar-items/

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # dics, ans = {}, []
        # for i in items1 + items2 :
        #     try : dics[i[0]] += i[1]
        #     except : dics[i[0]] = i[1]
        # for k, v in dics.items() : ans.append([k, v])
        # ans.sort()
        # return ans

        # items1.sort(), items2.sort()
        # idx, l1, l2 = 0, len(items1), len(items2)
        # for i in items2 :
        #     if idx >= l1 : items1.insert(idx, i); l1 += 1
        #     else :
        #         while idx < l1 and items1[idx][0] < i[0] : idx += 1
        #         if idx >= l1 or items1[idx][0] > i[0] : items1.insert(idx, i); l1 += 1
        #         elif items1[idx][0] == i[0] : items1[idx][1] += i[1]
        #     idx += 1
        # return items1

        return sorted((Counter({i[0] : i[1] for i in items1}) + Counter({i[0] : i[1] for i in items2})).items())