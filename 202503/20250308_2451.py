## https://leetcode.com/problems/odd-string-difference/

class Solution:
    def oddString(self, words: List[str]) -> str:
        ln, sub_ln, idx1, idx2 = len(words), len(words[0]), 0, 1
        lst1, lst2 = self.diff(words[0], sub_ln), []
        while idx2 < ln :
            if self.diff(words[idx2], sub_ln) == lst2 : return words[idx1]
            elif self.diff(words[idx2], sub_ln) == lst1 and lst2 != [] : return words[idx2-1]
            elif self.diff(words[idx2], sub_ln) != lst1 and lst2 == [] : lst2 = self.diff(words[idx2], sub_ln)
            idx2 += 1
        return words[idx2] if idx2 < ln else words[idx2-1]

    def diff(self, word, ln) :
        lst, idx = [], 1
        while idx < ln : lst.append(ord(word[idx])-ord(word[idx-1])); idx += 1
        return lst