class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        str1=s[::-1]
        count=0
        for i in str1:
            if i!=' ':
                count+=1
            else:
                break
        return count
        
        