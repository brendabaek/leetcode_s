## https://leetcode.com/problems/number-of-valid-words-in-a-sentence/

class Solution:
    def countValidWords(self, sentence: str) -> int:
        tokens = [token for token in sentence.split(" ") if token != ""]
        l, n, m, = "abcdefghijklmnopqrstuvwxyz", "0123456789-", "!.,"
        ans = 0
        for token in tokens :
            check, d_check = True, True
            i = len(token)-1
            if token[i] in n : continue
            else : i -= 1
            while i > 0 :
                if token[i] in l : i -= 1
                elif token[i] == "-" :
                    if d_check == False : check = False; break
                    if token[i-1] in l and token[i+1] in l : i -= 1; d_check = False
                    else : check = False; break
                else : check = False; break
            if i == 0 and token[i] not in l : check = False
            if check == True : ans += 1
        return ans