# my solution

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ans=[0]*26

        for c in s:
            ans[ord(c)-ord('a')]+=1
        for c in t:
            ans[ord(c)-ord('a')]-=1

        for i in range(len(ans)):
            if ans[i]!=0:
                return False
        return True
    
    