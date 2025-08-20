""" 
we have to find the max possible count of number "1" in binary array 
like in 1,1,1,0,0,1,1 so longerst here is 3

here the approach is pretty straight forward 

we count the num==1 and update the counter along with updating the maxi var
then we rest the the counter when we encouter "0"
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums):

        cnt=0
        maxi=0

        for num in nums:

            if num==1:
                cnt+=1
                maxi=max(cnt,maxi)

            else:
                cnt=0
        return maxi