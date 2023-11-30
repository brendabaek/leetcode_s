## https://leetcode.com/problems/rearrange-spaces-between-words/

class Solution:
    def reorderSpaces(self, text: str) -> str:
        ln, lst = len(text), []
        if text[0] == " " : cnt, tmp = 1, ""
        else : cnt, tmp = 0, text[0]
        for i in range(1, ln) :
            if text[i-1] == " " :
                if text[i] == " " : cnt += 1
                else : tmp += text[i]
            else :
                if text[i] == " " :
                    cnt += 1
                    lst.append(tmp)
                    tmp = ""
                else : tmp += text[i]
        if tmp != "" : lst.append(tmp)
        new_ln = len(lst) - 1
        if new_ln == 0 : return lst[0] + (" " * cnt)
        cnt1, cnt2 = " " * (cnt // new_ln), " " * (cnt % new_ln)
        ans = cnt1.join(lst) + cnt2
        return ans