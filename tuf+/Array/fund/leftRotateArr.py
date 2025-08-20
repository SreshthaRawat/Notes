# Left Rotate Array by One

""" 
To rotate an array by one position to the left, consider that the first element of the 
array will move to the last position, while all other elements shift one position to the left.
"""

class Solution:
    def rotateArrayByOne(self, nums):

        n=len(nums)
        
        temp=nums[0]

        for i in range(1,n):
            nums[i-1]=nums[i]

        nums[-1] = temp
        
