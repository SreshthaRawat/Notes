# my solution

""" 
so what basically we're doing in this quetion is that
we create an empty list with 0 as all 26 elements to rep the alphabet
so to check for the anagram we fill 1 instead of 0 in both s and t 
and then we match if the list of s and t have same amount of zero
if not we return false
 """

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
    
    