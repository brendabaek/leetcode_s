## https://leetcode.com/problems/unique-morse-code-words/

dics = {'a' : ".-", 'b' : "-...", 'c' : "-.-.", 'd' : "-..", 'e' : ".", 'f' : "..-.", 'g' : "--.",
        'h' : "....", 'i' : "..", 'j' : ".---", 'k' : "-.-", 'l' : ".-..", 'm' : "--", 'n' : "-.",
        'o' : "---", 'p' : ".--.", 'q' : "--.-", 'r' : ".-.", 's' : "...", 't' : "-", 'u' : "..-",
        'v' : "...-", 'w' : ".--", 'x' : "-..-",'y' : "-.--", 'z' : "--.."}

class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        lst, ans = [], 0
        for word in words :
            tmp = ''
            for w in word : tmp += dics[w]
            lst.append(tmp)
        return len(set(lst))