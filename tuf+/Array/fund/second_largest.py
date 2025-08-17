# ok so the brute force that you can do here is 
# just sort the array so the largest ele will be at last 
# and second largest will be at second last position
 for i in range(n-2, -1, -1):

            ''' If the current element is not
            equal to the largest element'''
            if nums[i] != largest:

                ''' Assign the current element 
                as the second largest and break'''
                secondLargest = nums[i]
                break





# more better approach here would be to eliminate sorting first
class Solution:

    def secondLargestElement(self, nums):
        # Get the length of the array
        n = len(nums)

        # Check if the array has less than 2 elements
        if n < 2:
            # If true, return -1 indicating there is no second largest element
            return -1 

        # Initialize variables to store the largest and second largest elements
        largest = float('-inf')
        secondLargest = float('-inf')

        # First traversal to find the largest element
        for i in range(n):
            largest = max(largest, nums[i])

        # Second traversal to find second largest element
        for i in range(n):
            if nums[i] > secondLargest and nums[i] != largest:
                secondLargest = nums[i]

        # Return the second largest element
        return -1 if secondLargest == float('-inf') else secondLargest
    

# optimal approach
'''To find the second-largest element in an array more efficiently, 
the idea is to perform the operation in a single traversal by making smart comparisons. 
This approach uses two variables to keep track of the largest and the second-largest elements 
while iterating through the array. This will help to find the second-largest element with just 
one pass throughout the array.'''

class Solution:
    def secondLargestElement(self, nums: List[int]) -> int:

        if len(nums) < 2:
            return -1

        largest =  float('-inf')
        second_largest =  float('-inf')

        for num in nums:

            if num > largest:
                second_largest = largest
                largest = num

            elif num > second_largest and num != largest:
                second_largest = num

        return -1 if second_largest == float('-inf') else second_largest




