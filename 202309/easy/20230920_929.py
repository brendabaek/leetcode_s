## https://leetcode.com/problems/unique-email-addresses/

class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        ans = set()
        for email in emails :
            name, domain = email.split('@')[0], email.split('@')[1]
            if len(domain.split('.com')) == 2 :
                try : name = name[:name.index("+")]
                except : pass
                name = name.replace('.', '')
                ans.add(name+'@'+domain)
        return len(ans)