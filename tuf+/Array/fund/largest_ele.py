# largest find, very basic as well just declare the
# first ele as the largest then iterate through 
# the array by comparing the largest and updating it with all i 

class Solution:
    def largestElement(self, nums):

        largest=nums[0]

        for i in range(len(nums)):

            if nums[i]>largest:
                largest=nums[i]

        return largest
        