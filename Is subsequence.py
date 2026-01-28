class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s=="":
            return True
        j=len(s)
        l=0
        for i in range(len(t)):
            if l<len(s) and s[l]==t[i]:
                l+=1  

        if l==j:
            return True
        return False