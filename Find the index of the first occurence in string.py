class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j=len(needle)
        i=0
        for k in haystack:
            ans=haystack[i:j]
            if ans==needle:
                return i
            i+=1
            j+=1
        return -1