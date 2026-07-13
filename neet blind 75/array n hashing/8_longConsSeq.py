# so the optimal approach is with hashsets that'll give us 0(1) lookup time
# ts and tc is 0(n)

# so the approach is we're going to take num from hashset, where num-1 is not in the hashset.

# after finding possibly one of many num-1 we'll start that as first element then in while loop 
# we'll do num+1 and take a pointer (curr) that'll count the consecutive num+1 (ex:1,2,3,4,...,n-1)

# after finding the largest curr we'll store that in res (res=max(curr,res))
# make sure you do that just outside while loop as inside while res gets updated every step and 
# even though only the final curr matters but it'll be nice to update it once per sequence only 
# and voila it's my first solution that i brute forced and it came out optimal xddd


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        arr= set(nums)
        res=1

        for num in arr:
            curr=1
            if num-1 not in arr:
                while num+1 in arr:
                    curr+=1
                    num+=1
                res=max(curr,res)
        return res






        